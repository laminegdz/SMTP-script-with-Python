🛠️ Key Features:

Uses SMTP (smtplib) to send emails.
Reads sender accounts from accounts.txt, where each line contains email:password.
Reads recipient emails from leads.txt.
Loads an HTML email body from email_body.html.
Cycles through sender accounts, attempting to send an email to each lead.
Removes successfully emailed leads from leads.txt to prevent duplicate sending.
Introduces a delay (2 seconds by default) between emails to avoid being flagged as spam.

🔄 Workflow:
Load sender accounts (accounts.txt).
Load recipient leads (leads.txt).
Load email body from email_body.html.
For each lead:
Try sending an email using available accounts.
If successful, remove the lead from leads.txt.
If no accounts succeed, print a failure message.
Loop until all leads are processed.

⚠️ Notes & Considerations:
SMTP Server & Credentials

Requires a valid SMTP server (smtp_server) and port (587 for TLS, 465 for SSL).
Works with providers like Gmail, Outlook, or custom SMTP servers.
If using Gmail, enable "Less secure apps" or generate an App Password.
Avoid Spam Flags

Use a reasonable delay (delay_between_emails) to prevent getting blocked.
Rotate sender accounts to distribute the load.
Avoid using too many identical emails, as providers may flag them.
Potential Improvements

Implement a retry mechanism for failed emails.
Log failures instead of printing them.
Use an SMTP pool instead of looping through accounts.

🚀 Use Case:
This script is useful for email marketing, outreach campaigns, and notifications, but should be used ethically and in compliance with anti-spam regulations (e.g., GDPR, CAN-SPAM Act).
