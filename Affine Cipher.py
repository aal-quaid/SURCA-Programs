def coprime(multiplier): #This function determines if the multiplier is coprime with 26 
    if (26<=multiplier):
        return False
    a = multiplier
    b = 26
    while a>0:
        x = b%a
        b = a
        a = x
    if b>1 and a==0:
        return False
    else:
        return True
    
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
    a = modInverse(multiplier)
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

def modInverse(multiplier): #While I understand the concept, I could not apply it to code. This function's algorithm is not mine
    for i in range(1, 26): #Taken from https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/ 
        if (((multiplier % 26) * (i % 26)) % 26 == 1):
            return i
    return -1
def main():
    print("Affine Cipher Program")
    shift = int(input("Enter shift: "))
    multiplier = int(input("Enter multiplier: "))
    isCoprime = coprime(multiplier)
    print(isCoprime)
    if isCoprime==True:
        choice = int(input("Enter 1 to encrypt a message, enter 2 to decrypt a message: "))
        if choice==1:
            encrypt(shift,multiplier)
        if choice==2:
            decrypt(shift,multiplier)
        else:
            print("Invalid Input. Please try again.") #Validates input
    else:
        print("Multiplier must be coprime with 26. Please try again.") #Multiplier must be coprime with 26 to properly encrypt/decrypt
main()