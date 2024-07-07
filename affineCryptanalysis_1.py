#This program finds the keys to the cipher with only the plainText and cipherText

import math

def keys(P, C):
    validValues = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]   #List of all possible values for A

    P = P.lower()
    C = C.lower()

    for i in range(len(P)-1):
        for j in range(i+1, len(P)):

            P1 = ord(P[i]) - ord('a')
            P2 = ord(P[j]) - ord('a')
            C1 = ord(C[i]) - ord('a')
            C2 = ord(C[j]) - ord('a')

            D = (P1 - P2) % 26
            if math.gcd(D, 26) != 1:    #Checks to see if D is relatively prime to 26
                continue

            inverseD = inverse(D)

            AKey = (inverseD * (C1 - C2)) % 26
            BKey = (inverseD * (P1*C2 - P2*C1)) % 26

            return AKey, BKey
    

    for A in validValues:               #Cycle through all possible values for A
        if C1 - C2 == (A * (P1-P2)) % 26:
            B = (C1 - (P1*A)) % 26      #Substite A into one of the equations to find B
            return A, B

def inverse(a):
    for num in range(1,26):
        if (num * a) % 26 == 1:
            return num

def main():

    P = input("Enter plainText (2 or more letters): ")
    C = input("Enter cipherText (2 or more letters): ")
    
    A, B = keys(P, C)

    print(f"\nThe Keys are: A = {A} and B = {B}")

main()