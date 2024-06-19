import math

def isValid(multiplier,shift): #checks if multiplier and shift are valid and if multiplier is coprime with 26
    if (multiplier<26 and multiplier>=1 and math.gcd(multiplier,26)==1 and shift>=1 and shift<26):
        return True 
    else:
        return False

def inverse(multiplier):  # This function finds the multiplicative inverse
    for num in range(1, 26):
        if (num * multiplier) % 26 == 1:
            return num
    return -1

def encrypt(shift,multiplier):
    plainText = input("Enter message to encrypt: ")
    encrypted = ""
    for letter in plainText:
        if letter.isupper():
            tempVar = ord(letter)-ord("A") #Temporary value sets letter between 0 and 25
            encrypted+=chr(ord("A")+((multiplier*tempVar)+shift)%26)
        elif letter.islower():
            tempVar = ord(letter)-ord("a")
            encrypted+=chr(ord("a")+((multiplier*tempVar)+shift)%26)
        else:
            encrypted+=letter #If the character isn't a letter, the character will be added back to the message
    print("Encrypted message:",encrypted)

def decrypt(shift,multiplier): 
    a = inverse(multiplier)
    plainText = input("Enter message to decrypt: ")
    decrypted = ""
    for letter in plainText:
        if letter.isupper():
            tempVar = ord(letter)-ord("A") 
            decrypted+=chr(ord("A")+(a*(tempVar-shift)%26))
        elif letter.islower():
            tempVar = ord(letter)-ord("a")
            decrypted+=chr(ord("a")+((a*(tempVar-shift)%26)))
        else:
            decrypted+=letter
    print("Decrypted message:",decrypted)

def main():
    print("Affine Cipher Program")
    x = int(input("Enter 1 to continue: "))
    while x==1:
        multiplier = int(input("Enter multiplier: "))
        shift = int(input("Enter shift: "))
        boolean = isValid(multiplier,shift)
        if boolean==True:
            choice = int(input("Enter 1 to encrypt a message, enter 2 to decrypt a message: "))
            if choice==1:
                encrypt(shift,multiplier)
            elif choice==2:
                decrypt(shift,multiplier)
        else:
            print("Invalid Input. Please Try Again")
        x = int(input("Enter 1 to continue, enter 0 to quit: "))
    print("Goodbye!")

main()
