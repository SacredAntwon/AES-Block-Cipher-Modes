# Author: Anthony Maida
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import sys
import argparse
# Create an instance of the argument parser
parser=argparse.ArgumentParser(description="Argument parser")
# Define the valid arguments
parser.add_argument("-key", type=str)       # The key
parser.add_argument("-encdec", type=int)    # Whether to encrypt or decrypt (0 = encrypt; 1 = decrypt)
parser.add_argument("-iv", type=str)        # The initialization vector
parser.add_argument("-infile", type=str)        # The name of the input file
parser.add_argument("-outfile", type=str)       # The name of the output file
# Parse the arguments
args = parser.parse_args()
# Grab the arguments
key = args.key.encode()     # The encryption key converted to bytes
encdec = args.encdec        # Whether to encrypt
iv = args.iv.encode()       # The IV in bytes
outFileName = args.outfile  # The name of the output file

cipher = AES.new(key, AES.MODE_OFB, iv)

print("OFB Mode")
# Open the input file
with open(args.infile, "rb") as inFile:
    # TODO create an instance of the AES in OFB mode class
    # TODO: Implement the encryption logic
    obj = inFile.read()
    if encdec == 0:
        encryptedData = cipher.encrypt(obj)
        f = open(outFileName,'wb')
        f.write(encryptedData) # writing to file
        f.close()

    # TODO: Implement the decryption logic
    elif encdec == 1:
        decryptedData = cipher.decrypt(obj)
        f = open(outFileName,'wb')
        f.write(decryptedData) # writing to file
        f.close()

    print(f"Output File: {outFileName}")

    print("Complete!")
