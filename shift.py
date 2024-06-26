#Assumption: 
#plaintext - lowercase letters only
#ciphertext - UPPER CASE LETTERS ONLY
def encryption(shift):
    cipherText = ""

    plainText = input("Enter text to encrypt: ")

    for letter in plainText:
        if letter == " ":
            cipherText += " "
        else:
            C = ord(letter) - (ord)('a')                # C = CipherText
            value = (C + shift) % 26
            cipherText += chr((ord)('A') + value)        # converts ascii value to a char
    
    return cipherText

def decryption(shift):
    plainText = ""

    cipherText = input("Enter text to decrypt: ")

    for letter in cipherText:
        if letter == " ":
            plainText += " "
        else:
            C = (ord)(letter) - (ord)('A')              # C = CipherText
            value = (C - shift) % 26
            plainText += chr((ord)('a') + value)         # converts ascii value to a char
    
    return plainText

def main():
    choice = 1

    while choice != 0:
        choice = int(input("\nEnter 1 to encrypt, 2 to decrypt and 0 to exit: "))

        if choice == 1:
            shift = int(input("Enter key: "))

            cipherText = encryption(shift)
            print("\nCipher Text = ", cipherText)

        elif choice == 2:
            shift = int(input("Enter key: "))
            
            plainText = decryption(shift)
            print("\nPlain Text = ", plainText)
    
    print("\nGood Bye!")


main()