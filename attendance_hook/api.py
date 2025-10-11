import frappe

@frappe.whitelist()
def login():
    # البحث عن اسم الموظف بناءً على المستخدم الحالي في الجلسة
    y = frappe.db.get_value("Employee", {"user_id": frappe.session.user}, "name")
    
    # التحقق مما إذا كان الموظف موجودًا
    if not y:
        return {"message": "Employee not found", "status": "error"}

    shift = frappe.get_doc("Employee", y)

    # تسجيل IN إذا كان الموظف موجودًا
    if shift:
        x = frappe.new_doc("Employee Checkin")
        x.employee = y
        x.log_type = "IN"
        x.insert()
        return {"message": f"Done IN {x.name}", "status": "success"}

@frappe.whitelist()
def logout():
    # البحث عن اسم الموظف بناءً على المستخدم الحالي في الجلسة
    y = frappe.db.get_value("Employee", {"user_id": frappe.session.user}, "name")
    
    # التحقق مما إذا كان الموظف موجودًا
    if not y:
        return {"message": "Employee not found", "status": "error"}

    shift = frappe.get_doc("Employee", y)

    # تسجيل OUT إذا كان الموظف موجودًا
    if shift:
        x = frappe.new_doc("Employee Checkin")
        x.employee = y
        x.log_type = "OUT"
        x.insert()
        return {"message": f"Done OUT {x.name}", "status": "success"}
