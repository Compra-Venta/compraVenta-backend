import smtplib, ssl

def send_email(email, base, quote, date, time, order_type, side, b_amount, stop):
    
    query_email = "teamcompraventa@gmail.com"
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "teamcompraventa@gmail.com"
    receiver_email = email
    #password = email_password
    message = f"""\
    Subject: Stoploss Order.
    Hello {email},
    New password has been set successfully for your account on Compra-Venta.
    For any queries contact {query_email}.
    New Password : {time}
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