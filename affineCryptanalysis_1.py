#This program finds the keys to the cipher with only the plainText and cipherText

#Assume the user will enter 2 or more letters for each text
import math

def keys(P, C):
    P = P.lower()
    C = C.lower()

    P1 = ord(P[0]) - ord('a')
    P2 = ord(P[1]) - ord('a')
    C1 = ord(C[0]) - ord('a')
    C2 = ord(C[1]) - ord('a')

    D = (P1 - P2) % 26

    if math.gcd(D, 26) != 1: #Checks to see if D is valid
        return False, False
    
    inverseD = inverse(D)

    A = (inverseD * (C1 - C2)) % 26
    B = (inverseD * (P1*C2 - P2*C1)) % 26

    return A, B

def inverse(a):
    for num in range(1,26):
        if (num * a) % 26 == 1:
            return num

def main():

    P = input("Enter plainText (2 or more letters): ")
    C = input("Enter cipherText (2 or more letters): ")
    
    A, B = keys(P, C)

    if A == False:
        print("Invalid Input. Please try again.")
    else:
        print(f"\nThe Keys are: A = {A} and B = {B}")

main()