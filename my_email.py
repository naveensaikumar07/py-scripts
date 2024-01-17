import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Log in to the SMTP server
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(smtp_username, to_email, message.as_string())

    print("Email sent successfully!")

# Replace these values with your own
subject = "Test Email"
body = "This is a test email sent using Python."
to_email = "nskumar9380@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "n.s.k9986431466@gmail.com"
smtp_password = input("your_password :")

# Call the function to send the email
send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password)
