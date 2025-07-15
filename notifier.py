# notifier.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVERS


def send_email(new_jobs):
    if not new_jobs:
        print("No new jobs found. No email sent.")
        return

    # Create email content
    subject = f"New Job Listings - {len(new_jobs)} jobs found!"
    body = "<h2>New Job Listings Found:</h2><ul>"

    for job in new_jobs:
        body += f'<li><a href="{job["link"]}">{job["title"]}</a> at {job["company"]} ({job["location"]})</li>'

    body += "</ul>"

    # Set up the MIME message
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(EMAIL_RECEIVERS)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {', '.join(EMAIL_RECEIVERS)}")
    except Exception as e:
        print(f"Failed to send email: {e}")
