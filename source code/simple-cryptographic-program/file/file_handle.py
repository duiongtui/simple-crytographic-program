from algorithms import algorithms_aes as aes
from algorithms import algorithms_des3 as des3
from algorithms import algorithms_rsa as rsa
from Crypto.Hash import SHA256 as sha
import os

AES = 0
DES3 = 1

def encrypt_file(filepath,folder2save_enc,key,algorithms = -1):
    file_name = os.path.basename(filepath)
    #Kiem tra su ton tai cua thu muc luu file ma hoa, tao neu khong co
    check_and_create_folder(folder2save_enc)

    if algorithms == AES:
        with open(filepath,"rb") as infile:
            with open(folder2save_enc+"/"+file_name+'.cipher',"wb") as outfile:
                origin = infile.read()
                origin_and_hash = origin + generate_hash(origin)
                enc = aes.encrypt_aes(origin_and_hash,key)
                outfile.write(enc)
                infile.close()
                outfile.close()

    elif algorithms == DES3:
        with open(filepath,"rb") as infile:
            with open(folder2save_enc+"/"+file_name+'.cipher',"wb") as outfile:
                origin = infile.read()
                origin_and_hash = origin + generate_hash(origin)
                enc = des3.encrypt_des3(origin_and_hash,key)
                outfile.write(enc)
                infile.close()
                outfile.close()
    else:
        raise ValueError("This type of algorithm isn't supported")


def decrypt_file(filepath,folder2save_dec,key,algorithms = -1):

    file_name = os.path.basename(filepath)
    check_and_create_folder(folder2save_dec)

    if algorithms == 0:
        with open(filepath,"rb") as infile:
            with open(folder2save_dec+"/" + "decrypted_" + (file_name[:-7]) ,"wb") as outfile:
                enc = infile.read()
                origin_and_hash = aes.decrypt_aes(enc,key)
                success,origin = check_hash(origin_and_hash)
                outfile.write(origin)
                infile.close()
                outfile.close()
    elif algorithms == 1:
        with open(filepath,"rb") as infile:
            with open(folder2save_dec+"/" + "decrypted_" + (file_name[:-7]) ,"wb") as outfile:
                enc = infile.read()
                origin_and_hash = des3.decrypt_des3(enc,key)
                success,origin = check_hash(origin_and_hash)
                outfile.write(origin)
                infile.close()
                outfile.close()
    else:
        raise ValueError("This type of algorithm isn't supported")
    return success

def encrypt_file_rsa(filepath,keypath,folder2save_enc):

    filename = os.path.basename(filepath)
    #Kiem tra su ton tai cua thu muc luu file ma hoa, tao neu khong co
    check_and_create_folder(folder2save_enc)

    with open(filepath,"rb") as infile:
            with open(folder2save_enc+"/"+ filename +'.cipher',"wb") as outfile:
                origin = infile.read()
                origin_and_hash = origin + generate_hash(origin)
                enc = rsa.encrypt_rsa(origin_and_hash,keypath)
                outfile.write(enc)
                infile.close()
                outfile.close()
def decrypt_file_rsa(filepath,keypath,folder2save_dec):
    filename = os.path.basename(filepath)
    check_and_create_folder(folder2save_dec)

    with open(filepath,"rb") as infile:
        with open(folder2save_dec+"/" + "decrypted_" + (filename[:-7]) ,"wb") as outfile:
            cipertext = infile.read()
            origin_and_hash = rsa.decrypt_rsa(cipertext,keypath)
            success,origin = check_hash(origin_and_hash)
            outfile.write(origin)
            infile.close()
            outfile.close()
    return success

def generate_hash(data_in):
    hash_func = sha.new()
    hash_func.update(data_in)
    hash_value = hash_func.digest()
    return hash_value

def check_hash(data_in):
    hash_value = data_in[-sha.digest_size:]
    hash_func = sha.new()
    hash_func.update(data_in[:-sha.digest_size])
    if hash_func.digest() == hash_value:
        return True,data_in[:-sha.digest_size]
    return False,data_in[:-sha.digest_size]

def check_and_create_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)