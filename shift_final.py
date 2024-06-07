"""
Assumption: 
plaintext - lowercase letters only
ciphertext - UPPER CASE LETTERS ONLY
"""
def encryption(shift):
    string = input("Enter message to encrypt: ")
    cipherText = ""

    for letter in string:
        if letter == " ":
            cipherText += " "
        else:
            num = (ord)(letter) - (ord)('a')
            new_num = (num + shift) % 26
            cipherText += chr((ord)('A') + new_num)
    
    return cipherText

def decryption(shift):
    string = input("Enter message to decrypt: ")
    plainText = ""

    for letter in string:
        if letter == " ":
            plainText += " "
        else:
            num = (ord)(letter) - (ord)('A')
            new_num = (num-shift) % 26
            plainText += chr((ord)('a') + new_num)
    
    return plainText

def main():
    print("Shift Cipher Program")

    choice = int(input("Enter 1 to continue, 0 to exit: "))

    while choice != 0:
        print ("\nEnter 1 to encrypt, 2 to decrypt and 0 to exit: ")
        choice = int(input(""))

        if choice == 1:
            shift = int(input("Enter shift: "))
            cipherText = encryption(shift)
            print("\nCipher Text = ", cipherText)

        elif choice == 2:
            shift = int(input("Enter shift: "))
            plainText = decryption(shift)
            print("\nPlain Text = ", plainText)
    
    print("\nGood Bye!")

main()