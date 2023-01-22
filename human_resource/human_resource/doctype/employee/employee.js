// Copyright (c) 2023, me and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee', {
//	refresh: function(frm) {
//	    function joinDate(){
//		    var today = new Date();
//            var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
//            return date;
//		}
//		frm.set_df_property("date_of_joining", "read_only", 1);
//		if (frm.is_new()) {
//        frm.set_value("date_of_joining", joinDate());
//		}
//        // set full name value and read only
//        function fullName(){
//		    var fullname = frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name;
//            return fullname;
//		}
//		frm.set_df_property("full_name", "read_only", 1);
//        frm.set_value("full_name", fullName());
//        // set age read only and give it value
//		function getAge(birthdate) {
//            var today = new Date();
//            var birthdate = new Date(birthdate);
//            var age = today.getFullYear() - birthdate.getFullYear();
//            var m = today.getMonth() - birthdate.getMonth();
//            if (m < 0 || (m === 0 && today.getDate() < birthdate.getDate())) {
//                age--;
//            }
//            return age;
//		}
//        frm.set_df_property("age", "read_only", 1);
//        frm.set_value("age", getAge(frm.doc.date_of_birth));
//	},
//	validate: function(frm) {
//	   // validate status
//	    if (frm.doc.status == "Active"){
//	        msgprint('Sorry, You Can Not Make Status Active');
//            throw('Sorry, You Can Not Make Status Active');
//	    }
//	   // validate age
//	    function getAge(birthdate) {
//            var today = new Date();
//            var birthdate = new Date(birthdate);
//            var age = today.getFullYear() - birthdate.getFullYear();
//            var m = today.getMonth() - birthdate.getMonth();
//            if (m < 0 || (m === 0 && today.getDate() < birthdate.getDate())) {
//                age--;
//            }
//            return age;
//		}
//
//	    if (getAge(frm.doc.date_of_birth) >= 60){
//            msgprint('Sorry, Your Age Is Too Old');
//            throw('Sorry, Your Age Is Too Old');
//        }
//        // validate of mobile number
//        if (frm.doc.mobile.length != 10) {
//            msgprint('Error, Mobile Must Be 10 numbers');
//            throw('Error, Mobile Must Be 10 numbers');
//        }
//        if (!frm.doc.mobile.startsWith('059')) {
//            msgprint('Error, Mobile Must Begin By 059**');
//            throw('Error, Mobile Must Begin By 059**');
//        }
//        // employee education must be at least 2 branches
//        if (frm.doc.employee_part.length < 2) {
//            msgprint('Sorry, Employee Part Must Be At Least 2 Branches');
//            throw('Sorry, Employee Part Must Be At Least 2 Branches');
//        }
//        }
	}
);
