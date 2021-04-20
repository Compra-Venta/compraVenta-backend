import uuid
from datetime import datetime 
import time

def generate_unique_string(email):

	a=uuid.uuid4().hex[:20]
	b=str(time.time())
	b1=b.split(".")[0]
	email=email.split(".")[0]
	c=str(a+b1+email)
	return c
#email= input('email:')
email='gh'
s1=generate_unique_string(email)
print(s1)
