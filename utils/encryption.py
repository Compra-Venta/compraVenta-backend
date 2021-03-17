from cryptography.fernet import Fernet

key = b'XCHPeZGaDLRGVzc79iXdc8rWG8z8O4KvPE3YgYK_JIE='

f = Fernet(key)
def encrypt_password(txt):
    txt = bytes(txt,'utf-8')
    return (f.encrypt(txt))

def decrypt_password(txt):
    return str(f.decrypt(txt).decode("utf-8") )


