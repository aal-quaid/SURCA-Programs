import math

def inverse(x):
    for num in range(1,26):
        if (num * x) % 26 == 1:
            return num
        
def decrypt(a, b, cipherText):
    cipherText = cipherText.upper()
    plainText = ""

    for letter in cipherText:

        if letter == " ":
            plainText += " "
        else:
            x = ord(letter) - ord('A')
            a_inverse = inverse(a)
            new_num = a_inverse * (x - b) % 26
            plainText += chr((ord)('A') + new_num)
    
    return plainText


def bruteForce(cipherText):
    A_list = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    for a in A_list:
        for b in range(26):
            print(decrypt(a, b, cipherText))
            print(f"A = {a}, B = {b}")

            userInput = int(input("Enter 1 to continue, 0 to quit: "))

            if userInput == 0:
                return

def main():
    cipherText = input("Enter cipher text: ")
    bruteForce(cipherText)
    print("Bye")

main()