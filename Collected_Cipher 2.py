# CS363
# Dr. Ting Gu
# Members: Sarah Fake, Samuel Niles, Ryan Ehmann
# Implementation of Cipher

def encrypt(plaintext, key):
    encrypted = ""
    letter = plaintext[7 % len(plaintext)]
    left = plaintext[6 % len(plaintext)]
    right = plaintext[8 % len(plaintext)]
    
    letterVal = ord(letter)
    leftVal = ord(left)
    rightVal = ord(right)
    
    
    if letterVal > leftVal and letterVal > rightVal:
        for char in plaintext:
            if (ord(char) % 2 == 0):
                encrypted += chr(ord(char) + int(key[0]) % 127)
            else: 
                encrypted += chr(ord(char) * int(key[1]) % 127)
                encrypted += chr(ord(char) + int(key[2]) % 127)
                                 
    elif letterVal < leftVal and letterVal < rightVal:
        for char in plaintext:
             encrypted += chr(ord(char) + int(key[3]) % 127)
    elif letterVal > leftVal and letterVal < rightVal: 
        for char in plaintext:
             encrypted += chr(ord(char) + int(key[4]) % 127)
    elif letterVal < leftVal and letterVal > rightVal:
        for char in plaintext:
             encrypted += chr(ord(char) + int(key[5]) % 127)
    else:
        for char in plaintext:
         encrypted += chr(ord(char) + int(key[6]) % 127)
    
       
    return encrypted
    
def decrypt(encrypted, key):
    decrypted = ""
    letter = encrypted[7 % len(encrypted)]
    left = encrypted[6 % len(encrypted)]
    right = encrypted[8 % len(encrypted)]
    
    letterVal = ord(letter)
    leftVal = ord(left)
    rightVal = ord(right)
    
    
    if letterVal > leftVal and letterVal > rightVal:
        i=0;
        while i < len(encrypted):
            if (ord(encrypted[i]) % 2 == 0): 
                decrypted += chr(ord(encrypted[i]) - int(key[0]) % 127)
                i+=1
            else: 
                i +=1
                decrypted += chr(ord(encrypted[i]) - int(key[1]) % 127)
                i += 1
                         
                
    elif letterVal < leftVal and letterVal < rightVal:
        for char in encrypted:
             decrypted += chr(ord(char) - int(key[2]) % 127)
    elif letterVal > leftVal and letterVal < rightVal: 
        for char in encrypted:
             decrypted += chr(ord(char) - int(key[3]) % 127)
    elif letterVal < leftVal and letterVal > rightVal:
        for char in encrypted:
             decrypted += chr(ord(char) - int(key[4]) % 127)
    else:
        for char in encrypted:
         decrypted += chr(ord(char) - int(key[5]) % 127)    
    
       
    return decrypted    

def main():
    
    text = input("Enter a phrase to be encrypted: ")
    
    prompt = input("Would you like to encrypt or decrypt (e/d)? ")
    
    
    encryptCode = open("encryptKey.txt",'r').read()
    decryptCode = open("decryptkey.txt",'r').read()
    
    numbersE = encryptCode.split("\n")
    numbersD = decryptCode.split("\n")
    
    '''Testing
    print(numbersE)
    print(numbersD)
    '''
    
    if prompt == 'e':
        encrypted = encrypt(text, numbersE)
        print("Encrypted Text: ", encrypted)
    elif prompt == 'd':
        decrypted = decrypt(text, numbersD)
        print("Decrypted Text: ", decrypted)
    
main()
