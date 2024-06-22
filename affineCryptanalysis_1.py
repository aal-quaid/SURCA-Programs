#This program finds the keys to the cipher with only the plainText and cipherText
#This program can only function with 2 letter texts

#Assume the user will only enter 2 letters for each text

def keys(P, C):
    P = P.lower()
    C = C.lower()

    P1 = ord(P[0]) - ord('a')
    P2 = ord(P[1]) - ord('a')
    C1 = ord(C[0]) - ord('a')
    C2 = ord(C[1]) - ord('a')

    D = (P1 - P2) % 26
    inverseD = inverse(D)

    A = (inverseD * (C1 - C2)) % 26
    B = (inverseD * (P1*C2 - P2*C1)) % 26

    return A, B

def inverse(a):
    for num in range(1,26):
        if (num * a) % 26 == 1:
            return num

def main():

    P = input("Enter plainText (2 letters): ")
    C = input("Enter cipherText (2 letters): ")
    
    A, B = keys(P, C)

    print(f"\nThe Keys are: A = {A} and B = {B}")

main()