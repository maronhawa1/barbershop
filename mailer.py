# 
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# המייל של המנהל – לשים פה את המייל שיקבל התראות
ADMIN_EMAIL = "maronhawa13@gmail.com"

# נמשוך את המפתח מהסביבה (Environment Variables ברנדר)
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")


def send_admin_email(name, phone, service, date, hour):
    if not SENDGRID_API_KEY:
        print("Missing SENDGRID_API_KEY, cannot send admin email")
        return

    subject = "תור חדש נקבע במספרה"
    body = f"""
נרשם תור חדש:

שם: {name}
טלפון: {phone}
שירות: {service}
תאריך: {date}
שעה: {hour}

מומלץ להיכנס לפאנל הניהול.
"""

    message = Mail(
        from_email=ADMIN_EMAIL,
        to_emails=ADMIN_EMAIL,
        subject=subject,
        plain_text_content=body,
    )

    sg = SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)


def send_client_email(client_email, name, service, date, hour):
    if not SENDGRID_API_KEY:
        print("Missing SENDGRID_API_KEY, cannot send client email")
        return

    subject = "אישור קביעת תור - מספרת ברבר שופ"
    body = f"""
שלום {name},

התור שלך נקבע בהצלחה!

טיפול: {service}
תאריך: {date}
שעה: {hour}

נשמח לראות אותך,
מספרת ברבר שופ 💈
"""

    message = Mail(
        from_email=ADMIN_EMAIL,
        to_emails=client_email,
        subject=subject,
        plain_text_content=body,
    )

    sg = SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)
