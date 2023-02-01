# Copyright (c) 2023, me and contributors
# For license information, please see license.txt

import frappe


@frappe.whitelist()
def any_function():
    return "this file created manually"
