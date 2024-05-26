def encryption(plainText):
    cipherText = ""

    plainText = plainText.upper()       # makes string upper case

    for i in plainText:
        if i == " ":
            cipherText += " "
        else:
            P = ord(i)                      # converts char to ascii value
            C = ((P - 65) + 3) % 26         # C = CipherText, P = plainText
            value = C + 65
            cipherText += chr(value)        # converts ascii value to a char
    
    return cipherText

def decryption(cipherText):
    plainText = ""

    cipherText = cipherText.lower()     # makes string lower case
    for i in cipherText:
        if i == " ":
            plainText += " "
        else:
            P = ord(i)                      # converts char to ascii value
            C = ((P - 97) - 3) % 26         # C = CipherText, P = plainText
            value = C + 97
            plainText += chr(value)         # converts ascii value to a char
    
    return plainText

def main():
    choice = int(input("Enter 0 to encrypt and 1 to decrypt: "))

    if choice == 0:
        plainText = input("Enter text to encrypt: ")
        cipherText = encryption(plainText)
        print("\nCipher Text = ", cipherText)

    elif choice == 1:
        cipherText = input("Enter text to decrypt: ")
        plainText = decryption(cipherText)
        print("\nPlain Text = ", plainText)

    else:
        print("\nInvalid Input")


main()