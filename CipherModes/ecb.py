# Author: Anthony Maida
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
import sys
import argparse
# Create an instance of the argument parser
parser=argparse.ArgumentParser(description="Argument parser")
# Define the valid arguments
parser.add_argument("-key", type=str)       # The key
parser.add_argument("-encdec", type=int)    # Whether to encrypt or decrypt (0 = encrypt; 1 = decrypt)
parser.add_argument("-infile", type=str)        # The name of the input file
parser.add_argument("-outfile", type=str)       # The name of the output file
# Parse the arguments
args = parser.parse_args()
# Grab the arguments
key = args.key.encode()     # The encryption key converted to bytes
encdec = args.encdec        # Whether to encrypt
outFileName = args.outfile  # The name of the output file

cipher = AES.new(key, AES.MODE_ECB)

print("ECB Mode")
# Open the input file
with open(args.infile, "rb") as inFile:
    # TODO create an instance of the AES in ECB mode class
    # TODO: Implement the encryption logic
    obj = inFile.read()
    if encdec == 0:
        encryptedData = cipher.encrypt(pad(obj, 16))
        f = open(outFileName,'wb')
        f.write(encryptedData) # writing to file
        f.close()

    # TODO: Implement the decryption logic
    elif encdec == 1:
        decryptedData = unpad(cipher.decrypt(obj), 16)
        f = open(outFileName,'wb')
        f.write(decryptedData) # writing to file
        f.close()

    print(f"Output File: {outFileName}")

    print("Complete!")
