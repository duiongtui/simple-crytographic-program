from algorithms import algorithms_aes as aes
from algorithms import algorithms_des3 as des3
from algorithms import algorithms_blowfish as blowfish
from algorithms import algorithms_rsa as rsa
from Crypto.Hash import SHA256 as sha

def encrypt_file(filepath,key,algorithms = -1):
    
    if algorithms == 0:
        with open(filepath,"rb") as infile:
            with open(filepath+'.cipher',"wb") as outfile:
                origin = infile.read()
                enc = aes.encrypt_aes(origin,key)
                outfile.write(enc)
                infile.close()
                outfile.close()
    elif algorithms == 1:
        with open(filepath,"rb") as infile:
            with open(filepath+'.cipher',"wb") as outfile:
                origin = infile.read()
                enc = des3.encrypt_des3(origin,key)
                outfile.write(enc)
                infile.close()
                outfile.close()
    elif algorithms == 2:
        with open(filepath,"rb") as infile:
            with open(filepath+'.cipher',"wb") as outfile:
                origin = infile.read()
                enc = blowfish.encrypt_blowfish(origin,key)
                outfile.write(enc)
                infile.close()
                outfile.close()
    else:
        raise ValueError("This type of algorithm isn't supported")
def decrypt_file(filepath,key,algorithms = -1):
    if algorithms == 0:
        with open(filepath,"rb") as infile:
            with open("decrypted_" + (filepath[:-7]) ,"wb") as outfile:
                enc = infile.read()
                origin = aes.decrypt_aes(enc,key)
                outfile.write(origin)
                infile.close()
                outfile.close()
    elif algorithms == 1:
        with open(filepath,"rb") as infile:
            with open("decrypted_" + (filepath[:-7]) ,"wb") as outfile:
                enc = infile.read()
                origin = des3.decrypt_des3(enc,key)
                outfile.write(origin)
                infile.close()
                outfile.close()
    elif algorithms == 2:
        with open(filepath,"rb") as infile:
            with open("decrypted_" + (filepath[:-7]) ,"wb") as outfile:
                enc = infile.read()
                origin = blowfish.decrypt_blowfish(enc,key)
                outfile.write(origin)
                infile.close()
                outfile.close()
    else:
        raise ValueError("This type of algorithm isn't supported")

def encrypt_file_rsa(filepath,keypath):
    
    with open(filepath,"rb") as infile:
            with open(filepath+'.cipher',"wb") as outfile:
                origin = infile.read()
                enc = rsa.encrypt_rsa(origin,keypath)
                outfile.write(enc)
                infile.close()
                outfile.close()
def decrypt_file_rsa(filepath,keypath):
      with open(filepath,"rb") as infile:
            with open("decrypted_" + (filepath[:-7]) ,"wb") as outfile:
                cipertext = infile.read()
                plaintext = rsa.decrypt_rsa(cipertext,keypath)
                outfile.write(plaintext)
                infile.close()
                outfile.close()

def generate_hash(data_in):
    hash_func = sha.new()
    hash_func.update(data_in)
    hash_value = hash_func.digest()
    return hash_value

def check_hash(data_in):
    print(len(data_in))
    hash_value = data_in[-sha.digest_size:]
    hash_func = sha.new()
    hash_func.update(data_in[:-sha.digest_size])
    if hash_func.digest() == hash_value:
        return True
    return False