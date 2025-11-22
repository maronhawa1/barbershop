import smtplib
from email.mime.text import MIMEText

# ---- הגדרות ----
ADMIN_EMAIL = "maronhawa13@gmail.com"
APP_PASSWORD = "bnnjcjinhqytwurv"  # הסיסמה הצהובה מגוגל

def send_admin_email(name, phone, service, date, hour):
    subject = "תור חדש נקבע במספרה"
    body = f"""
נרשם תור חדש:

שם: {name}
טלפון: {phone}
שירות: {service}
תאריך: {date}
שעה: {hour}

כדאי לבדוק במערכת הניהול.
"""

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = ADMIN_EMAIL
    msg["To"] = ADMIN_EMAIL

    # שליחה
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(ADMIN_EMAIL, APP_PASSWORD)
        server.sendmail(ADMIN_EMAIL, ADMIN_EMAIL, msg.as_string())
def send_client_email(client_email, name, service, date, hour):
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

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = ADMIN_EMAIL
    msg["To"] = client_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(ADMIN_EMAIL, APP_PASSWORD)
        server.sendmail(ADMIN_EMAIL, client_email, msg.as_string())
