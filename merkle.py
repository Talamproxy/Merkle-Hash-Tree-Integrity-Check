#!/usr/bin/python3
import glob, os, hashlib 


class Merkle_tree:
    os.chdir("/home/kali/Desktop/merkle/Merkle-Hash-Tree-Integrity-Check")
    hashArray = [] 
    for file in glob.glob("*.txt"):
        binary_file=open(file, 'rb').read()
        hash=hashlib.md5(binary_file).hexdigest()
        hashArray.append(hash)

    if(len(hashArray)%2!=0):
            hashArray.append(hashArray[-1])
     
    while(len(hashArray)>1):
        j=0
        for i in range(0, len(hashArray)-1):
            f = str(hashArray[i]+hashArray[i+1])
            hashArray[j]=hashlib.md5(f.encode()).hexdigest()
            print(f)
            i+=2
            j+=1
        print(hashArray)

        remainder=i-j
        del hashArray[-remainder:]

    
