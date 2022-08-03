// Copyright (c) 2022, Aakvatech and contributors
// For license information, please see license.txt


frappe.ui.form.on("Building", {
    	refresh: function(frm) {
    		if(frm.doc.building_name !== ""){
			frappe.call({
        			method:'propms.property_management_solution.doctype.building.building.n_units',
        			args: {
            				'building_name': frm.doc.building_name,
      		        	},
       		callback: function(r) {
				frm.set_value("no_of_units", r.message);
			}
        		});
        		
        		frappe.call({
        			method:'propms.property_management_solution.doctype.building.building.available_units',
        			args: {
            				'building_name': frm.doc.building_name,
      		        	},
       		callback: function(r) {
				frm.set_value("available_units", r.message);
			}
        		});
        	}
    	}
});


