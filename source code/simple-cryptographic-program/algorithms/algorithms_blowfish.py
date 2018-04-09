from Crypto.Cipher import Blowfish
from Crypto import Random

def pad(s, block_size):
    # Dam bao kich thuoc cua file nhap vao la boi cua AES.block_size
    padding_size = block_size - len(s) % block_size
    return s + b'\0' * padding_size,padding_size

def encrypt_blowfish(message,key):
    iv = Random.new().read(Blowfish.block_size)
    cipher = Blowfish.new(key,Blowfish.MODE_CFB,iv)

    padded_mess, padding_size = pad(message,Blowfish.block_size)

    return iv + cipher.encrypt(padded_mess) + bytes(padding_size)

def decrypt_blowfish(ciphertext,key):
    iv = ciphertext[:Blowfish.block_size]
    cipher = Blowfish.new(key,Blowfish.MODE_CFB,iv)

    message = cipher.decrypt(ciphertext[Blowfish.block_size:-1])
    # *-1 de dung cho cau lenh ke tiep
    padding_size = ciphertext[-1]*(-1)
    # Ban chat cau nay la tu dau den vi tri -padding_size, padding_size da duoc *-1 o cau lenh truoc
    if padding_size == 0:
        return message
    else:
        return message[:padding_size]