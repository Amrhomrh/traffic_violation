# Copyright (c) 2025, Amr and contributors
# For license information, please see license.txt
import frappe
from frappe import _


def execute(filters=None):
	columns, data = [
				{
			"label": _("Number Plate"),
			"fieldname": "document_number",
			"fieldtype": "Link",
			"options": "Car Card",
			"width": 150,
		},
		{
			"label": _("Full Name"),
			"fieldname": "full_name",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Violation Name"),
			"fieldname": "violation_name",
			"fieldtype": "Link",
			"options": "Violation Type",
			"width": 140,
		},
	], []
	return columns, data


