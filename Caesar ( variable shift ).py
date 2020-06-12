'''
Author:  Dinh ANh Nguyen
Created:  Jan 2020
Description: Caesar Cipher with variable shift
'''
def encode (keyString):
    msg = input("Enter text to encode: ")
    keyIndex = 0
    newmsg = str("")
    
    for ch in msg:

            key = ord(keyString[keyIndex % len(keyString)])
            newch = ord(ch) + key

            #if newch goes out of extended ascii table, reutrn to beginning and skip invisible chars
            if newch > 255:
                newch -= 224
                
            newmsg += chr(newch)
            keyIndex += 1
    
    #shift characters in string to the right by len(keyString)
    newmsg = shift(newmsg, len(keyString))
    print("Ciphertext: " + newmsg)
    
def decode (keyString):
    msg = input("Enter text to decode: ")
    
    #shift msg chrs back to original location w/ -len(keyString)
    msg = shift(msg, -len(keyString))
    
    keyIndex = 0
    newmsg = str("")
    
    for ch in msg:
        #key changes for each character in message, converts chr to int value
        #wraps around to avoid out of bounds if msg is longer than key
        key = ord(keyString[keyIndex % len(keyString)])
        
        newch = ord(ch) - key
        
        #if newch goes into invisible characters wrap around to end of extended ascii
        if newch < 32:
            newch +=224

        
        newmsg += chr(newch)
        keyIndex += 1 


    print("Plaintext: " + newmsg)

#shifts elements of arr n units ( + = right, - = left)
def shift(arr, n):
    n = n % len(arr)
    return arr[n:] + arr[:n]
    
def main():

    keyFile = open("key.txt", 'r')
    key = keyFile.readline()
    keyFile.close()

    while(True):
        command = int(input("Decrypt (0), encrypt (1), or exit (-1): "))
    
        if command == 1:
            encode(key)
        elif command == 0:
            key = input("Enter key: ")
            decode(key)
        elif command == -1:
            return
        else:
            print("ERROR: invalid command")
        
main()
