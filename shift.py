def encryption(plainText, key):
    cipherText = ""

    plainText = plainText.upper()       # makes string upper

    for letter in plainText:
        if letter == " ":
            cipherText += " "
        else:
            C = ((ord(letter) - (ord)('A')) + key) % 26         # C = CipherText
            value = C + (ord)('A')
            cipherText += chr(value)        # converts ascii value to a char
    
    return cipherText

def decryption(cipherText, key):
    plainText = ""

    cipherText = cipherText.lower()

    for letter in cipherText:
        if letter == " ":
            plainText += " "
        else:
            C = ((ord)(letter) - (ord)('a') - key) % 26         # C = CipherText
            value = C + (ord)('a')
            plainText += chr(value)         # converts ascii value to a char
    
    return plainText

def main():
    choice = 1

    while choice != 0:
        choice = int(input("\nEnter 1 to encrypt, 2 to decrypt and 0 to exit: "))

        if choice == 1:
            plainText = input("Enter text to encrypt: ")
            key = int(input("Enter key: "))

            cipherText = encryption(plainText, key)
            print("\nCipher Text = ", cipherText)

        elif choice == 2:
            cipherText = input("Enter text to decrypt: ")
            key = int(input("Enter key: "))
            
            plainText = decryption(cipherText, key)
            print("\nPlain Text = ", plainText)
    
    print("\nGood Bye!")


main()