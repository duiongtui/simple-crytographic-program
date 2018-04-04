
from Crypto.Hash import MD5
import file.file_handle as file_handle
import os
from algorithms import algorithms_rsa as rsa
AES = 0
DES3 = 1

if __name__ == "__main__":
    key = "sang"
    padded_key = MD5.new()
    padded_key.update(key.encode())
    
    #file_handle.encrypt_file("C:/Users/Sang/Desktop/New folder/_MDP4147.jpg","C:/Users/Sang/Desktop/New folder/enc",padded_key.digest(),AES)
    success = file_handle.decrypt_file("C:/Users/Sang/Desktop/New folder/enc/_MDP4147.jpg.cipher","C:/Users/Sang/Desktop/New folder/dec",padded_key.digest(),AES)
    
    #rsa.generate_key("C:/Users/Sang/Desktop/New folder/key")
    #file_handle.encrypt_file_rsa("C:/Users/Sang/Desktop/New folder/plaintext.txt","C:/Users/Sang/Desktop/New folder/key/public_key.pem","C:/Users/SUN/Desktop/New folder/enc")
    #success = file_handle.decrypt_file_rsa("C:/Users/Sang/Desktop/New folder/enc/plaintext.txt.cipher","C:/Users/Sang/Desktop/New folder/key/private_key.pem","C:/Users/Sang/Desktop/New folder/dec")
    print(success)
    #print(os.getcwd().replace(os.path.sep,'/'))