#from Crypto.Random import get_random_bytes
from Crypto.Hash import MD5
import file.file_handle as file_handle
from algorithms import algorithms_rsa as rsa

AES = 0
DES3 = 1
BLOWFISH = 2

if __name__ == "__main__":
    key = "sang"
    padded_key = MD5.new()
    padded_key.update(key.encode())
    
    #rsa.generate_key()
    #rsa.encrypt_rsa("plaintext.txt",".\output\pulic_key.pem")
    #rsa.decrypt_rsa("plaintext.txt.cipher",".\output\private.pem")
    #file_handle.encrypt_file_rsa("plaintext.txt",".\output\pulic_key.pem")
    #file_handle.decrypt_file_rsa("plaintext.txt.cipher",".\output\private.pem")

    with open("plaintext.txt","rb") as check:
        data = check.read()
        hashvalue = file_handle.generate_hash(data)
        print(len(hashvalue))
        if file_handle.check_hash(data + hashvalue):
            print("Hash success")
        else:
            print("Hash fail")