import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def send_email(sender_email, sender_name, sender_password, smtp_server, smtp_port, lead_email, html_body):
    msg = MIMEMultipart('alternative')
    msg['From'] = f"{sender_name} <{sender_email}>"
    msg['To'] = lead_email
    msg['Subject'] = "replace" 

    part = MIMEText(html_body, 'html')
    msg.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, lead_email, msg.as_string())
            print(f"Email sent to {lead_email} from {sender_email}")
            return True
    except Exception as e:
        print(f"Failed to send email to {lead_email} from {sender_email}. Error: {e}")
        return False

if __name__ == "__main__":
    smtp_server = "replace"
    smtp_port = 587
    sender_name = "replace"
    delay_between_emails = 2

    with open("accounts.txt", "r") as file:
        accounts = [line.strip().split(':') for line in file.readlines()]

    with open("leads.txt", "r") as file:
        leads = [line.strip() for line in file.readlines()]

    with open("email_body.html", "r") as file:
        html_body = file.read()

    for lead_email in leads[:]: 
        email_sent = False
        for account in accounts:
            sender_email, sender_password = account
            if send_email(sender_email, sender_name, sender_password, smtp_server, smtp_port, lead_email, html_body):
                email_sent = True
                leads.remove(lead_email)  
                with open("leads.txt", "w") as file:
                    for lead in leads:
                        file.write(f"{lead}\n")
                break
        if not email_sent:
            print(f"Failed to send email to {lead_email} with all accounts.")
        time.sleep(delay_between_emails)

print("-----finished-----")
