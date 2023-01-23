# Copyright (c) 2023, me and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import date_diff


class LeaveApplication(Document):
    def validate(self):
        self.get_leave_days()
        self.get_leave_balance()
        self.selected_days_balance_availability()

    def on_submit(self):
        self.submit_update_allocation()

    def on_cancel(self):
        self.cancel_update_allocation()

    def get_leave_days(self):
        total_days = date_diff(self.to_date, self.from_date) + 1
        self.total_leave_days = total_days

    def get_leave_balance(self):
        result = frappe.db.get_value("Leave Allocation",
                                     {"employee_name": self.employee_name, "leave_type": self.leave_type},
                                     "total_leaves_allocated")
        self.leave_balance_before_application = result

    def selected_days_balance_availability(self):
        query_from_date = frappe.db.get_value("Leave Allocation",
                    {"employee_name": self.employee_name, "leave_type": self.leave_type}, "from_date")
        query_to_date = frappe.db.get_value("Leave Allocation",
                    {"employee_name": self.employee_name, "leave_type": self.leave_type}, "to_date")
        if self.from_date >= str(query_from_date) and self.to_date <= str(query_to_date):
            if self.total_leave_days > self.leave_balance_before_application:
                frappe.throw("Error, Please Select Duration Not More Allowed")
        else:
            frappe.throw("Error, Please Select Duration Within Allowed")

    def submit_update_allocation(self):
        new_balance = self.leave_balance_before_application - self.total_leave_days
        return frappe.db.set_value("Leave Allocation", self.employee_name, "total_leaves_allocated", new_balance)

    def cancel_update_allocation(self):
        result = frappe.db.get_value("Leave Allocation",
                                     {"employee_name": self.employee_name, "leave_type": self.leave_type},
                                     "total_leaves_allocated")
        new_balance = result + self.total_leave_days
        return frappe.db.set_value("Leave Allocation", self.employee_name, "total_leaves_allocated", new_balance)

