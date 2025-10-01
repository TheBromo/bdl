
from cryptography.hazmat.primitives import hashes

import sys

InputString = sys.argv[1]
Data = InputString.encode()

#Digest is the object that manages the "hashing lifecycle"
# 1 - Initilaize
# 2 - Update the value to be hashed.
# 3 - Finalize: compute the hash.

digest = hashes.Hash(hashes.SHA3_256())
digest.update(Data)
HashVal = digest.finalize() #Data type of result is bytes

#Let's convert it to what one usually needs
# A simple string that encodes the HEX value.

Hash = HashVal.hex() #This function returns the HEX-encoding as a simple string.

#Casting the hash value as unsigned integer.
#Byte order big means that a byte sequence say b'\x0F\x00' is processed as 0F00 (as one would write it on paper). The "big" parts come first. Signed = False means we just want to know what the byte-string means as a positive number.

HashAsInteger = int.from_bytes(HashVal, byteorder='big', signed = False) 

#Print everything:
print("Hash value as HEX string: " + Hash)
print("Hash Value as Integer: " + str(HashAsInteger))

