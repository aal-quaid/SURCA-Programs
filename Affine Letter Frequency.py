import math 
import itertools as iTools

def inverse(x):
    for i in range(1,26):
        if (i * x) % 26 == 1:
            return i

def letterFrequency(string): #This function puts each character as a key in a dictionary  
    frequency = {}           #with its value pair being its frequency
    for char in string: 
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char] = 1
        if " " in frequency:
            frequency.pop(" ") #removes spaces from the dictionary
    return frequency

def sortByFrequency(dict): #this function returns a list sorted from most to least frequent
    x = list(dict.items()) #creates a list containing tuples of each item's key and value pair
    x.sort(key=lambda item: item[1]) #sorts by frequency in ascending order using lambda function
    x.reverse() 
    return x

def findKeys(c1,c2,p1,p2):
    C1 = ord(c1.lower()) - ord('a')
    C2 = ord(c2.lower()) - ord('a')
    P1 = ord(p1.lower()) - ord('a')
    P2 = ord(p2.lower()) - ord('a')
    D = (P1-P2)%26
    tOrf = True if math.gcd(D,26)==1 else False
    if tOrf==False:
        return False,False
    D_inverse = inverse(D)
    A = D_inverse * (C1 - C2)%26
    if math.gcd(A,26)!=1:
        return False,False #Validates A and ends the function early if it's not coprime with 26
    B = (D_inverse*((P1*C2) - (P2*C1)))%26     
    return A,B

def decrypt(string,list1,list2):
    for x,y,p1,p2 in iTools.product(list1,list1,list2,list2):
        if x==y:
            continue
        if p1==p2:
            continue
        c1 = x[0]
        c2 = y[0]           
        A,B = findKeys(c1,c2,p1,p2)
        if A!=False:
            A_inverse = inverse(A)
            plainText = ""
            for letter in string:
                if letter.isupper():
                    tempVar = ord(letter)-ord('A') 
                    plainText+=chr(ord('A')+(A_inverse*(tempVar-B)%26))
                elif letter.islower():
                    tempVar = ord(letter)-ord('a')
                    plainText+=chr(ord('a')+((A_inverse*(tempVar-B)%26)))
                else:
                    plainText+=letter
            print(plainText,A,B)
            z = input("Enter c to continue: ")
        else: 
            continue
        if z=='c' or z=='C':
            None
        else:
            break 

def main():
    print("Affine Cipher Key Finder & Decryption")
    englishFrequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
    cipherText = input("Enter encrypted message: ")
    frequency = sortByFrequency(letterFrequency(cipherText))
    decrypt(cipherText,frequency,englishFrequency)
    print("Goodbye!")
   

main()