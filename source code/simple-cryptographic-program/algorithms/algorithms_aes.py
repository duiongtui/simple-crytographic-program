from Crypto.Cipher import AES
from Crypto import Random

def pad(s):
    # Dam bao kich thuoc cua file nhap vao la boi cua AES.block_size
    padding_size = AES.block_size - len(s) % AES.block_size
    return s + b'\0' * padding_size,padding_size

def encrypt_aes(message,key):
    # khoi tao aes
    padded_mess, padding_size = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key,AES.MODE_CBC,iv)
    
    # padding_size ho tro viec loai bo phan bu duoc them vao khi pad 1 file
    print(len(iv + cipher.encrypt(padded_mess) + bytes([padding_size])))
    return iv + cipher.encrypt(padded_mess) + bytes([padding_size])

def decrypt_aes(ciphertext,key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key,AES.MODE_CBC,iv)

    # Vi tri -1 la padding_size
    print(len(ciphertext[AES.block_size:-1]))
    print(len(ciphertext))
    message = cipher.decrypt(ciphertext[AES.block_size:-1])
    padding_size = ciphertext[-1] * (-1)
    return message[:padding_size]