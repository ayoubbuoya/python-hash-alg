import hashlib

''' 

THIS TOOL IS MADE
 
By :> Ayoub Buoya

'''
#Just Learning Some Hash Algoritms

#To Print All Hash Algorithms,You Can Do This
hash_alg=hashlib.algorithms_guaranteed
print("All Hash Algorithms : ")
print(hash_alg)
print("")
#This Md5 Hash 
msg="ayoub buoya".encode()
print("Message :\n",msg)
print("Md5 Encryption :")
print(hashlib.md5(msg).hexdigest())
#This Sha1 Hash 
print("Sha1 Encryption :")
print(hashlib.sha1(msg).hexdigest())
#This sha256 Hash 
print("Sha256 Encryption :")
print(hashlib.sha256(msg).hexdigest())

# You Can Do More Algorithm With Same Method 
 