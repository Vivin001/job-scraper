import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_SENDER, EMAIL_PASSWORD


def send_email(name, to_email, job_results):
    subject = f"Hi {name}, here are your job listings!"

    if isinstance(job_results, list):
        body = f"<h2>Hi {name}, here are the latest jobs for you:</h2><ul>"
        for job in job_results:
            body += f'<li><a href="{job["link"]}">{job["title"]}</a> at {job["company"]} ({job["location"]})</li>'
        body += "</ul>"
    else:
        body = f"<p>{job_results}</p>"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, to_email, msg.as_string())
        server.quit()
        print(f"✅ Email sent successfully to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
