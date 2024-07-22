import math
from itertools import product

englishFrequency = [        #most frequent letters that appear in sentences 
    'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U', 
    'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z'
]

letter_dict = {             #A dictionary to keep track of all the letter in the cipher text
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
    'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 
    'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
    'Y': 0, 'Z': 0
}

def findFrequency(cipherText):      #This function finds the most accuring letter in the cipher text
    global letter_dict

    for letter in cipherText:
        letter_dict[letter] += 1
    
    letter_dict = dict(sorted(letter_dict.items(), key=lambda item: item[1], reverse=True))
    return list(letter_dict.keys())     # return the list of frequent letter in the cipher text


def cipherKeys(C1, C2, P1, P2):

    C1 = ord(C1) - ord('A')
    C2 = ord(C2) - ord('A')
    P1 = ord(P1) - ord('A')
    P2 = ord(P2) - ord('A')

    D = (P1 - P2) % 26

    if math.gcd(D, 26) != 1:
        return False, False     #Ends function if D isn't relatively prime with 26
    
    D_inverse = inverse(D)
    A = D_inverse * (C1 - C2) % 26

    if math.gcd(A, 26) != 1:
        return False, False     #Ends function if A isn't relatively prime with 26
    
    B = (D_inverse * ((P1 * C2) - (P2 * C1))) % 26

    return A, B

def inverse(a):         #Finds the inverse of value 'a'
    for num in range(1,26):
        if (num * a) % 26 == 1:
            return num
    return -1

def decrypt(cipherText, cipherFrequency, englishFrequency):
    for C1, C2, P1, P2 in product(cipherFrequency, cipherFrequency, englishFrequency, englishFrequency):
        if C1 == C2 or P1 == P2:        #pervents any repititon
            continue

        A, B = cipherKeys(C1, C2, P1, P2)

        if A == False:      #if A is invalid we will try another combination, if not we will continue
            continue
        else:
            plainText = ""

            for letter in cipherText:       #Creates plainText
                if letter == " ":
                    plainText += " "
                else:
                    x = ord(letter) - ord('A')
                    A_inverse = inverse(A)
                    new_num = A_inverse * (x - B) % 26
                    plainText += chr((ord)('A') + new_num)

            print(f"A = {A}, B = {B}")
            print(plainText)

            userInput = int(input("Is the text valid? If so, enter 1. If not, enter 0: "))       #Asks the user if the sentence is valid
            print("\n")

        if userInput == 0:
            continue
        else:
            print("Thank You!")
            break

def main():
    global englishFrequency

    print("Letter Frequency Program:\n")

    cipherText = input("Enter cipher text: ")
    cipherText = cipherText.upper()

    cipherFrequency = findFrequency(cipherText)

    decrypt(cipherText, cipherFrequency, englishFrequency)
    
main()