from algorithms import algorithms_aes as aes

def encrypt_file(filepath,key,algorithms = None):
    with open(filepath,"rb") as infile:
        with open(filepath+'.cipher',"wb") as outfile:
            origin = infile.read()
            enc = aes.encrypt_aes(origin,key)
            outfile.write(enc)
            infile.close()
            outfile.close()

def decrypt_file(filepath,key,algorithms = None):
    with open(filepath,"rb") as infile:
        with open("decrypted_" + (filepath[:-7]) ,"wb") as outfile:
            enc = infile.read()
            origin = aes.decrypt_aes(enc,key)
            outfile.write(origin)
            infile.close()
            outfile.close()