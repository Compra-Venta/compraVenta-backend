import smtplib, ssl
from utils.config import email_password

def send_email(email, base, quote, date, time, order_type, side, b_amount, stop,name):
    
    query_email = "teamcompraventa@gmail.com"
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "teamcompraventa@gmail.com"
    receiver_email = email
    password = email_password
    message = f"""\
    Subject: Stoploss Order.


    Hi,

    Your order with order id {name} has been placed successfully.
    You order details are as follows.

    1. Base asset: {base}
    2. Quote asset: {quote}
    3. Date: {date}
    4. Time: {time}
    5. Order_type: {order_type}
    6. Side: {side}
    7. Base amount: {b_amount}

    For any queries contact {query_email}.

    Till then keep your trading quest on.!!
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
