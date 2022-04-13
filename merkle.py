#!/usr/bin/python3
import glob, os, hashlib

from more_itertools import value_chain 


class Merkle_tree:
    #Points in the directory in which the files to be hashed are 
    os.chdir("/home/kali/Desktop/merkle/Merkle-Hash-Tree-Integrity-Check")
    hashArray = [] 
    #Loops all .txt files in the folder generating their hash and storing them in an array called hashArray 
    for file in glob.glob("*.txt"):
        binary_file=open(file, 'rb').read()
        hash=hashlib.md5(binary_file).hexdigest()
        hashArray.append(hash)

    print("This is the hash value of all the file in the folder:")
    print(hashArray)
    #Checks to see if the item is an array are even, if not it appends the last item in the array to make it even 
    if(len(hashArray)%2!=0):
            hashArray.append(hashArray[-1])
     
    #This function concatinates all the files in the array by combining two items in an array and finding its hash value
    #The size of the array is round on the while loop untill only one top hash is left
    while(len(hashArray)>1):
        j=0
        for i in range(0, len(hashArray)-1):
            f = str(hashArray[i]+hashArray[i+1])
            hashArray[j]=hashlib.md5(f.encode()).hexdigest()
            
            i+=2
            j+=1
        del hashArray[j:]

    if (len(hashArray)==1):
        print("This is the Top Hash:") 
        print(hashArray)
    
if __name__ == "__main__":
     Merkle_tree()
