# Copyright (c) 2022, Aakvatech and contributors
# For license information, please see license.txt

import frappe
import datetime
from frappe.model.document import Document

class Building(Document):
	pass
	
@frappe.whitelist()
def n_units(building_name= None):
	no_of_units = frappe.db.count('Units',filters={"building_name": building_name})
	return no_of_units
			
@frappe.whitelist()		
def available_units(building_name= None):
	available_units = frappe.db.count('Units',filters={"building_name": building_name, "units_status": "Available"})
	return available_units


