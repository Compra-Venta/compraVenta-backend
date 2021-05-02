import smtplib, ssl
from utils.config import email_password

def send_token(email, name, token):
    
    query_email = "teamcompraventa@gmail.com"
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "teamcompraventa@gmail.com"
    receiver_email = email
    password = email_password
    message = f"""\
    Subject: Registration.

    Hello {name},
    {token} is your registration token for your email verification.
    For any queries contact {query_email}.
    Thanks
    """

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        try:
            server.sendmail(sender_email, receiver_email, message)
            return True
        except:
            return False
