def encrypt(shift):
    string = input("Enter message to encrypt: ")
    encrypted = ""
    for letter in string:
        num = (ord)(letter)-(ord)('a')
        new_num = (num+shift)%26
        encrypted+=chr((ord)('A')+new_num)
    return encrypted

def decrypt(shift):
    string = input("Enter message to decrypt: ")
    decrypted = ""
    for letter in string:
        num = (ord)(letter)-(ord)('a')
        new_num = (num-shift)%26
        decrypted+=chr((ord)('A')+new_num) 
    return decrypted

def main():
    print("Shift Cipher Program")
    full_message = ""
    choice = int(input("Enter 1 to continue: "))
    shift = int(input("Enter shift: "))
    while(choice==1):
        print("Enter 1 to encrpyt a message\nEnter 2 to decrpyt a message")
        x = int(input(""))   
        if x==1:
            string = encrypt(shift)
            # print("Encrypted message:",string)
            full_message+=string
        elif x==2:
            string = decrypt(shift)
            # print("Decrypted message:",string)
            full_message+=string
        else:
            print("Invalid input")#Validates input for the choice
        choice = int(input("Enter 1 to continue, enter 2 to quit: "))
        full_message+=" "
    print("Full message:",full_message)
main()
