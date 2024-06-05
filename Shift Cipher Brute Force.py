def bruteForce(string,shift):
    message = ""
    for letter in string:
        if letter==" ":
            message+=" "
        else:
            num = (ord)(letter)-(ord)('a')
            new_num = (num-shift)%26
            message+=chr((ord)('A')+new_num)
    return message
def main():
    print("Brute Force Decryption Program")
    string = input("Enter message to decrypt: ")
    for i in range(1,26):
        message = bruteForce(string,i)
        print("Message for shift",i,"is",message)
main()