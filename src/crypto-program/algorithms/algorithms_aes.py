from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import MD5

def pad(s, block_size):
    # Dam bao kich thuoc cua file nhap vao la boi cua AES.block_size
    padding_size = block_size - len(s) % block_size
    return s + b'\0' * padding_size,padding_size

def encrypt_aes(message,key_in):

    hashFunc = MD5.new()
    hashFunc.update(bytes(key_in,'utf-8'))
    key = hashFunc.digest()

    # khoi tao aes
    padded_mess, padding_size = pad(message,AES.block_size)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key,AES.MODE_CFB,iv)
    
    # padding_size ho tro viec loai bo phan bu duoc them vao khi pad 1 file
    #print(len(iv + cipher.encrypt(padded_mess) + bytes([padding_size])))
    
    return iv + cipher.encrypt(padded_mess) + bytes([padding_size])

def decrypt_aes(ciphertext,key_in):

    hashFunc = MD5.new()
    hashFunc.update(bytes(key_in,'utf-8'))
    key = hashFunc.digest()

    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key,AES.MODE_CFB,iv)

    # Vi tri -1 la padding_size
    message = cipher.decrypt(ciphertext[AES.block_size:-1])
    padding_size = ciphertext[-1] * (-1)
    if padding_size == 0:
        return message
    else:
        return message[:padding_size]