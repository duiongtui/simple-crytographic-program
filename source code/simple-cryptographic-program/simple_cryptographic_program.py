from algorithms.algorithms_aes import *
from Crypto.Random import get_random_bytes
import file.file_handle as file_handle

if __name__ == "__main__":
    
    key = get_random_bytes(32)
    message = "look at me"
    
    #cipher = encrypt_aes(message,key)
    #print(cipher)
    #plain = decrypt_aes(cipher,key)
    #print(plain)

    file_handle.encrypt_file("plaintext.txt",key)
    file_handle.decrypt_file("plaintext.txt.cipher",key)

    #file_handle.encrypt_file("dive-into-python3.pdf",key)
    #file_handle.decrypt_file("dive-into-python3.pdf",key)

    #file_handle.encrypt_file("_MDP4147.jpg",key)
    #file_handle.decrypt_file("_MDP4147.jpg",key)