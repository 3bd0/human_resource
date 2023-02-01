# Copyright (c) 2023, me and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_timedelta, time_diff
from frappe.auth import get_logged_user
from datetime import timedelta


class Attendance(Document):
	def on_submit(self):
		self.check_work_hours()

	def check_work_hours(self):

		if self.check_in and self.check_out:
			query = frappe.get_doc('Attendance Settings')
			start_time = get_timedelta(query.start_time)
			end_time = get_timedelta(query.end_time)
			working_hours = timedelta(hours=query.working_hours_threshold_for_absent)
			late_entry = timedelta(minutes=query.late_entry_grace_period)
			early_exit = timedelta(minutes=query.early_exit_grace_period)
			allowed_check_in = start_time + late_entry
			allowed_check_out = end_time - early_exit
			work_day = end_time - start_time
			if working_hours:
				if time_diff(str(allowed_check_in), self.check_in) >= timedelta(0) and time_diff(self.check_out, str(allowed_check_out)) >= timedelta(0):
					self.work_hours = work_day.total_seconds()/3600
					# self.work_hours = working_hours.total_seconds()/3600
				elif time_diff(str(allowed_check_in), self.check_in) >= timedelta(0) and time_diff(str(allowed_check_out), self.check_out) > timedelta(0):
					calc_early_exit = allowed_check_out - get_timedelta(self.check_out)
					self.work_hours = (work_day - calc_early_exit).total_seconds()/3600
				elif time_diff(self.check_in, str(allowed_check_in)) > timedelta(0) and time_diff(self.check_out, str(allowed_check_out)) >= timedelta(0):
					calc_late_start = get_timedelta(self.check_in) - allowed_check_in
					self.work_hours = (work_day - calc_late_start).total_seconds()/3600
				else:
					calc_early_exit = allowed_check_out - get_timedelta(self.check_out)
					calc_late_start = get_timedelta(self.check_in) - allowed_check_in
					self.work_hours = (work_day - calc_late_start - calc_early_exit).total_seconds()/3600
				self.late_hours = work_day.total_seconds()/3600 - self.work_hours
				if working_hours == timedelta(0):
					self.status = "Present"
				elif working_hours.total_seconds()/3600 > self.work_hours:
					self.status = "Absent"
				else:
					self.status = "Present"
			else:
				frappe.throw("Please Insert Working Hours Threshold for Absent")
		else:
			frappe.throw("Please Insert Check In & Check Out")


@frappe.whitelist()
# def create_attendance(attendance_date, check_in, check_out):
def create_attendance(attendance_date, check_in, check_out):
	session_user = get_logged_user()
	emp = frappe.db.sql(f""" select name from tabEmployee where user = '{session_user}' """, as_dict=True)
	employee_name = emp[0].name
	doc = frappe.get_doc({
		"doctype": "Attendance",
		"employee": employee_name,
		"attendance_date": attendance_date,
		"check_in": check_in,
		"check_out": check_out})
	doc.insert()
	return "Attendance Successfully Created"
