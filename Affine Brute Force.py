import math

def inverse(x):
    for i in range(1,26):
        if (i * x) % 26 == 1:
            return i
        
def bruteForce(string):
    for a in range(1,26,2):
        if a==13: 
            continue
        for b in range(26):
            print(decrypt(a,b,string))
            x = input("Enter c to continue, q to quit: ")
            if x=='Q' or x=='q':
                return

            
def decrypt(a,b,string):
    a_inv = inverse(a)
    decrypted = ""
    for letter in string:
        if letter.isupper():
            decrypted+=chr(ord("A")+(a_inv*((ord(letter)-ord("A"))-b)%26))
        elif letter.islower():
            decrypted+=chr(ord("a")+((a_inv*((ord(letter)-ord("a"))-b)%26)))
        else:
            decrypted+=letter
    return decrypted

def main():
    cipherText = input("Enter cipher text: ")
    bruteForce(cipherText)
    print("Goodbye!")

main()