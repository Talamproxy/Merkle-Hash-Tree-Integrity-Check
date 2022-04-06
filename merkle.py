#!/usr/bin/python3
import glob, os
from hashlib import md5, sha1


class Merkle_tree:
    os.chdir("/home/kali/Desktop/merkle/Merkle-Hash-Tree-Integrity-Check")
    hashArray = [] 
    for file in glob.glob("*.txt"):
        binary_file=open(file, 'rb').read()
        hash=md5(binary_file).hexdigest()
        hashArray.append(hash)
        print(hashArray)
    
