import math

def inverse(x):
    for i in range(1,26):
        if (i * x) % 26 == 1:
            return i

def findKeysWithPairs(plainText,cipherText):
    for i in range(len(plainText)-1):
        P1 = ord(plainText[i].lower()) - ord('a')
        print(P1)
        P2 = ord(plainText[i+1].lower()) - ord('a')
        C1 = ord(cipherText[i].lower()) - ord('a')
        C2 = ord(cipherText[i+1].lower()) - ord('a')
        D = (P1-P2)%26
        if math.gcd(D,26)==1: #Checks to see if D is valid
            D_inverse = inverse(D)
            A = (D_inverse * (C1 - C2))%26
            B = (D_inverse*(P1*C2 - P2*C1))%26       
            return A,B   #ends function 
    return False, False #sends invalid input to move to the next method

def equationSubtraction(plainText,cipherText):
    for i in range(len(plainText)-1):
        cTarget = (ord(cipherText[i+1].lower())-ord('a'))-(ord(cipherText[i].lower())-ord('a'))
        pTarget = (ord(plainText[i+1].lower())-ord('a'))-(ord(plainText[i].lower())-ord('a'))
        for j in range(1,25,2):
            if pTarget*j%26==cTarget:
                A = j
                C2 = ord(cipherText[i+1].lower())-ord('a')
    B = (C2-(A*10))%26
    return A,B
    
def main():
    plainText = input("Enter plain text: ")
    cipherText = input("Enter cipher text: ")
    A,B = findKeysWithPairs(plainText,cipherText)
    if A==False:
        A,B = equationSubtraction(plainText,cipherText)
    print("The keys are A =",A,"and B =",B)
main()
