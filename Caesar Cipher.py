def encrypt(letter_list):
    string = input("Enter message to encrypt: ")
    encrypted = ""
    for letter in string:
        for i in range(len(letter_list)):
            if letter.isupper() and letter==letter_list[i]:
                encrypted+=letter_list[(i+3)%26]
                break #break statements terminate the loop after the correct letter has been found and added
            elif letter.islower() and letter==letter_list[i].lower():
                encrypted+=letter_list[(i+3)%26].lower()
                break 
            elif letter==" ":
                encrypted+=" "
                break
    return encrypted

def decrypt(letter_list):
    string = input("Enter message to decrypt: ")
    decrypted = ""
    for letter in string:
        for i in range(len(letter_list)):
            if letter.isupper() and letter==letter_list[i]:
                decrypted+=letter_list[(i-3)%26]
                break
            elif letter.islower() and letter==letter_list[i].lower():
                decrypted+=letter_list[(i-3)%26].lower()
                break
            elif letter==" ":
                decrypted+=" "
                break
    return decrypted

def main():
    #letter_list sets letters equal to their place in the alphabet minus 1. E.g. A=0, Z=25
    letter_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    print("Ceasar Cipher Program")
    print("Enter 1 to encrpyt a message\nEnter 2 to decrpyt a message")
    choice = int(input(""))   
    if choice==1:
        string = encrypt(letter_list)
        print("Encrypted message:",string)
    elif choice==2:
        string = decrypt(letter_list)
        print("Decrypted message:",string)
    else:
        print("Invalid input")#Validates input for the choice
main()