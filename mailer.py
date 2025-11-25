# mailer.py
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

ADMIN_EMAIL = "no-reply@maron-forms.com"   # הדומיין המאומת שלך
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")


def send_admin_email(name, phone, service, date, hour):
    if not SENDGRID_API_KEY:
        print("Missing SENDGRID_API_KEY, cannot send admin email")
        return

    subject = "תור חדש נקבע במספרה"
    body = f"""
נרשמה בקשת תור חדשה:

שם: {name}
טלפון: {phone}
שירות: {service}
תאריך: {date}
שעה: {hour}

כדאי להיכנס לפאנל הניהול ולאשר/לבטל.
"""

    message = Mail(
        from_email=ADMIN_EMAIL,
        to_emails="maronhawa13@gmail.com",   # המייל שלך
        subject=subject,
        plain_text_content=body,
    )

    sg = SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)


def send_client_email(client_email, name, service, date, hour, status):
    if not SENDGRID_API_KEY:
        print("Missing SENDGRID_API_KEY, cannot send client email")
        return

    if status == "pending":
        subject = "קיבלנו את בקשת התור - מספרת ברבר שופ"
        body = f"""
שלום {name},

בקשתך לקביעת תור נקלטה במערכת וממתינה לאישור.

טיפול: {service}
תאריך: {date}
שעה מבוקשת: {hour}

לאחר האישור תקבל הודעה נוספת.

מספרת ברבר שופ 💈
"""
    elif status == "approved":
        subject = "התור שלך אושר - מספרת ברבר שופ"
        body = f"""
שלום {name},

התור שלך אושר!

טיפול: {service}
תאריך: {date}
שעה: {hour}

נתראה,
מספרת ברבר שופ 💈
"""
    elif status == "canceled":
        subject = "עדכון לגבי התור - מספרת ברבר שופ"
        body = f"""
שלום {name},

לצערנו התור שביקשת לא אושר / בוטל.

טיפול: {service}
תאריך: {date}
שעה: {hour}

ניתן לקבוע מועד חדש דרך האתר.

מספרת ברבר שופ 💈
"""
    else:
        return

    message = Mail(
        from_email=ADMIN_EMAIL,
        to_emails=client_email,
        subject=subject,
        plain_text_content=body,
    )

    sg = SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)
 
