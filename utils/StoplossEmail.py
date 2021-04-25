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
    Your stoploss order with base {base} , quote {quote}, on date {date} at time {time}
    and order type {order_type}, side {side} with base amount {b_amount} has been successful.
    For any queries contact {query_email}.
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