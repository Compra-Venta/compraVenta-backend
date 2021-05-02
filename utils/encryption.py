from cryptography.fernet import Fernet

key = b'XCHPeZGaDLRGVzc79iXdc8rWG8z8O4KvPE3YgYK_JIE='

conversions = {"a":""}

d = {'a': '5', 'b': 'A', 'c': '*', 'd': 'B', 'e': 'C', 'f': 'f', 'g': '&', 'h': 'D', 'i': 'E', 'j': '^', 'k': 'l', 'l': 'n', 'm': '1', 'n': '6', 'o': 'z', 'p': '%', 'q': 'F', 'r': 'k', 's': 'm', 't': 'o', 'u': 'g', 'v': 'G', 'w': 'j', 'x': 'a', 'y': 'H', 'z': '7', 'A': 'h', 'B': 'I', 'C': 'J', 'D': 'i', 'E': 'b', 'F': '3', 'G': 'K', 'H': 'L', 'I': '2', 'J': '4', 'K': 'M', 'L': 'p', 'M': 'N', 'N': '8', 'O': 'O', 'P': 'P', 'Q': 'e', 'R': 'c', 'S': 'q', 'T': '0', 'U': '$', 'V': 't', 'W': 'Q', 'X': 'y', 'Y': 's', 'Z': 'v', '0': 'R', '9': 'S', '8': 'u', '7': '7', '6': 'r', '5': '9', '4': 'T', '3': 'd', '2': 'U', '1': 'V', '@': '@', '$': 'Q', '%': 'w', '^': 'X', '&': 'Y', '*': 'x'}

f = Fernet(key)
def encrypt_password(txt):
    txt = bytes(txt,'utf-8')
    return (f.encrypt(txt))

def decrypt_password(txt):
    return str(f.decrypt(txt).decode("utf-8") )

def encrypt_token(token):
    result = ""
    for i in range(len(token)):
        result+=d[token[i]]
    return result


