from utils.password_generator import generate_password
from utils.send_email import send_email
def send_recovery_email(email, name, password):
    send_email(email, name, password)