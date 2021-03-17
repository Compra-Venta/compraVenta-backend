import random
def generate_password():
    options = "abcdefghijklmnopqrstuvwxyz"
    options += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    options+= '0123654789'
    options += '@$%^&*'

    new_password = ""
    for i in range(10):
        n = random.randint(0,len(options)-1)
        new_password+=options[n]
    return new_password