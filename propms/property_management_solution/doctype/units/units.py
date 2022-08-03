# Copyright (c) 2022, Aakvatech and contributors
# For license information, please see license.txt

import datetime


import frappe
from frappe.model.document import Document

class Units(Document):
	def validate(self):
		if self.contract_start_date and self.contract_end_date:
			if datetime.date.today() < self.contract_start_date:
				self.units_status = "Booked"
			elif self.contract_start_date <= datetime.date.today() <= self.contract_end_date:
				self.units_status = "On lease"
		else:
			self.units_status = "Available"
			

		


