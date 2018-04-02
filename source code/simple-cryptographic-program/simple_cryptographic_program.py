#from Crypto.Random import get_random_bytes
from Crypto.Hash import MD5
import file.file_handle as file_handle

AES = 0
DES3 = 1

if __name__ == "__main__":
    key = "sang"

    padded_key = MD5.new()
    padded_key.update(key.encode())
    #cipher = encrypt_aes(message,key)
    #print(cipher)
    #plain = decrypt_aes(cipher,key)
    #print(plain)

    #file_handle.encrypt_file("plaintext.txt",key)
    #file_handle.decrypt_file("plaintext.txt.cipher",key)

    #file_handle.encrypt_file("dive-into-python3.pdf",padded_key.hexdigest())
    #file_handle.decrypt_file("dive-into-python3.pdf.cipher",padded_key.hexdigest())

    #file_handle.encrypt_file("_MDP4147.jpg",padded_key.digest(),AES)
    #file_handle.decrypt_file("_MDP4147.jpg.cipher",padded_key.digest(),AES)

    #file_handle.encrypt_file("_MDP4147.jpg",padded_key.digest(),DES3)
    file_handle.decrypt_file("_MDP4147.jpg.cipher",padded_key.digest(),DES3)