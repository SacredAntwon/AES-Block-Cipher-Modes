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
parser.add_argument("-tagfile", type=str)        # The initialization vector
parser.add_argument("-infile", type=str)        # The name of the input file
parser.add_argument("-outfile", type=str)       # The name of the output file
parser.add_argument("-noncefile", type=str) # The size of the block (in bits!)
# Parse the arguments
args = parser.parse_args()
# Grab the arguments
key = args.key.encode()     # The encryption key converted to bytes
encdec = args.encdec        # Whether to encrypt
tagFile = args.tagfile      # The tag file
nonceFile = args.noncefile  # The nonce file
outFileName = args.outfile  # The name of the output file

print("GCM Mode")
# Open the input file
with open(args.infile, "rb") as inFile:
    # TODO create an instance of the AES in GCM mode class
    # TODO: Implement the encryption logic
    obj = inFile.read()
    if encdec == 0:
        cipher = AES.new(key, AES.MODE_GCM)
        # Generate a nonce
        nonce = cipher.nonce
        nfile = open(nonceFile, "wb")
        nfile.write(nonce)
        nfile.close()
        # Encrypt and generate the MAC
        encryptedData, tag = cipher.encrypt_and_digest(obj)
        # Save the tag to the file
        tfile = open(tagFile, "wb")
        tfile.write(tag);
        tfile.close()
        # Save ciphertext
        f = open(outFileName,'wb')
        f.write(encryptedData) # writing to file
        f.close()

        print(f"Output File: {outFileName}, {nonceFile}, {tagFile}")

    # TODO: Implement the decryption logic
    elif encdec == 1:
        # Fetch the nonce from the file
        nonce = open(nonceFile, "rb").read()
        # Fetch the tag from the file
        tag = open(tagFile, "rb").read()
        cipher = AES.new(key, AES.MODE_GCM, nonce)
        decryptedData = cipher.decrypt(obj)
        f = open(outFileName,'wb')
        f.write(decryptedData) # writing to file
        f.close()
        # Verify the authenticity
        try:
                cipher.verify(tag)
                print("The plaintext is authentic")
        except:
            print("Wrong key or the integrity was compromised")

        print(f"Output File: {outFileName}")

    print("Complete!")
