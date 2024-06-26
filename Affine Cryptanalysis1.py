#Assumption is that two lowercase letters will be entered as the plain text and cipher text
import math 

def findKeys(plainText,cipherText):
    P1 = ord(plainText[0]) - ord('a')
    P2 = ord(plainText[1]) - ord('a')
    C1 = ord(cipherText[0]) - ord('a')
    C2 = ord(cipherText[1]) - ord('a')
    
    D = (P1-P2)%26
    
    if math.gcd(D,26)!=1: #Checks to see if D is valid
        return False,False #ends function early 
    
    D_inverse = inverse(D)
    
    A = (D_inverse * (C1 - C2))%26
    B = (D_inverse*(P1*C2 - P2*C1))%26       
    
    return A,B    

def inverse(x):
    for i in range(1,26):
        if (i * x) % 26 == 1:
            return i
        
def main():
    plainText = input("Enter plain text: ")
    cipherText = input("Enter cipher text: ")
    A,B = findKeys(plainText,cipherText)
    if A==False:
        print("There was an error. Please try again")
    else:
        print("The keys are A =",A,"and B =",B)

main()
