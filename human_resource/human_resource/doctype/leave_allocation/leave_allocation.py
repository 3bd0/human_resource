# Copyright (c) 2023, me and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LeaveAllocation(Document):
	def validate(self):
		self.date_order()
		self.duplicated_allocation()

	def date_order(self):
		if self.from_date > self.to_date:
			frappe.throw("Error, From Date Must Be Before To Date")
		else:
			return 1

	def duplicated_allocation(self):
		query = frappe.db.get_all("Leave Allocation",
						filters={'employee': 'Emp001', 'from_date': ['!=', self.from_date], 'to_date': ['!=', self.to_date]},
						fields=['from_date', 'to_date', 'leave_type'])
		for q in query:
			from_date = str(q.from_date)
			to_date = str(q.to_date)
			if q.leave_type == self.leave_type:
				if to_date >= self.from_date >= from_date or to_date >= self.to_date >= from_date:
					frappe.throw("Error, You Can't Make Duplicated Or Overlapping Allocation")
