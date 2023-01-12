# AES-Block-Cipher-Modes

Different AES Block Cipher Modes that was done for a final project in my cryptrography class.

## Use Example

_CFB_
Encryption: python3 cfb.py -key 1234567890abcdfg -iv 534567890abcdeds -blocksize 16 -infile file.txt -outfile file.enc -encdec 0

Decryption: python3 cfb.py -key 1234567890abcdfg -iv 534567890abcdeds -blocksize 16 -infile file.enc -outfile file.dec -encdec 1

_ECB_
Encryption: python3 ecb.py -key 1234567890abcdfg -infile file.txt -outfile file.enc -encdec 0

Decryption: python3 ecb.py -key 1234567890abcdfg -infile file.enc -outfile file.dec -encdec 1

_OFB_
Encryption: python3 ofb.py -key 1234567890abcdfg -iv 534567890abcdeds -infile file.txt -outfile file.enc -encdec 0

Decryption: python3 ofb.py -key 1234567890abcdfg -iv 534567890abcdeds -infile file.enc -outfile file.dec -encdec 1

_CTR_
Encryption: python3 ctr.py -key 1234567890abcdfg -noncefile noncefile.bin -infile file.txt -outfile file.enc -encdec 0

Decryption: python3 ctr.py -key 1234567890abcdfg -noncefile noncefile.bin -infile file.enc -outfile file.dec -encdec 1

_CBC_
Encryption: python3 cbc.py -key 1234567890abcdfg -iv 534567890abcdeds -infile file.txt -outfile file.enc -encdec 0

Decryption: python3 cbc.py -key 1234567890abcdfg -iv 534567890abcdeds -infile file.enc -outfile file.dec -encdec 1

_GCM_
Encryption: python3 gcm.py -key 1234567890abcdfg -tagfile tagfile.bin -noncefile noncefile.bin -infile file.txt -outfile file.enc -encdec 0

Decryption: python3 gcm.py -key 1234567890abcdfg -tagfile tagfile.bin -noncefile noncefile.bin -infile file.enc -outfile file.dec -encdec 1
