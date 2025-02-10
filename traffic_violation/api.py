import frappe
from frappe import _
from datetime import datetime

@frappe.whitelist(allow_guest=False)  # يمنع الوصول بدون صلاحيات
def create_violation(number_plate, violation_date, violation_name, location_violation):
    """
    دالة لتسجيل مخالفة مرورية جديدة.
    
    :param number_plate: رقم اللوحة (مُرتبط بـ Car Card).
    :param violation_date: تاريخ المخالفة.
    :param violation_name: نوع المخالفة.
    :param location_violation: موقع المخالفة.
    :return: رسالة نجاح أو خطأ.
    """
    # التحقق من البيانات
    if not number_plate or not violation_date:
        frappe.throw(_("Number Plate و Violation Date مطلوبان!"))

    # تحويل تنسيق التاريخ من dd-mm-yyyy HH:MM:SS إلى yyyy-mm-dd HH:MM:SS
    try:
        dt = datetime.strptime(violation_date, "%d-%m-%Y %H:%M:%S")
        violation_date = dt.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        frappe.throw(_("تنسيق تاريخ المخالفة غير صحيح! يرجى استخدام dd-mm-yyyy HH:MM:SS"))

    # جلب بيانات Car Card
    try:
        car_card = frappe.get_doc("Car Card", number_plate)
    except frappe.DoesNotExistError:
        frappe.throw(_("Car Card غير موجودة! تأكدي من الـ ID: {0}").format(number_plate))

    # إنشاء وثيقة Violations
    violation = frappe.get_doc({
        "doctype": "Violations",
        "document_number": number_plate,
        "violation_date": violation_date,
        "violation_name": violation_name,
        "location_violation": location_violation,
        "full_name": car_card.full_name,
        "national_number": car_card.national_number,
        "plate_type": car_card.plate_type,
        "plate_number": car_card.plate_number,
        "chassis_namber": car_card.chassis_number,
    })
    violation.insert()
    
    return {
        "message": "تم تسجيل المخالفة بنجاح!",
        "violation_id": violation.name
    }