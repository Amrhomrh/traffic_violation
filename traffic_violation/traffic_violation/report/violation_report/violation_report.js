// Copyright (c) 2025, Amr and contributors
// For license information, please see license.txt

frappe.query_reports["Violation Report"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(),-1),
			"reqd": 1,
			"width": "100px"
		},
		{
			"fieldname":"to_date",
			"label": __("To"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "100px"
		},
		{
			"fieldname":"violation_name",
			"label": __("Violation Name"),
			"fieldtype": "Link",
			"options": "Violation Type",
			"width": "100px"
		},


	]
};
