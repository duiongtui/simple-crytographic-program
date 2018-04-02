from algorithms import algorithms_aes as aes
from algorithms import algorithms_des3 as des3

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
    else:
        raise ValueError("This type of algorithm isn't supported")