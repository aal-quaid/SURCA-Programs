import math

def coprime(a, b):          #This function checks to see if 'a' and 'b' are valid
    cond1 = math.gcd(a, 26) == 1
    cond2 = 1 <= a <= 25
    cond3 = 0 <= b <= 25

    if cond1 and cond2 and cond3 == True:
        return True
    else:
    	return False

def inverse(a):         #This function finds the multiplicative inverse
    for num in range(1,26):
        if (num * a) % 26 == 1:
            return num

def encrypt(a, b):
    cipherText = ""

    string = input("Enter message to decrypt: ")

    for letter in string:
        if letter == " ":
            cipherText += " "
        else:
            x = ord(letter) - ord('a')
            new_num = (a*x + b) % 26
            cipherText += chr((ord)('A') + new_num)

    return cipherText

def decrypt(a, b):
    plainText = ""

    string = input("Enter message to decrypt: ")

    for letter in string:
        if letter == " ":
            plainText += " "
        else:
            x = ord(letter) - ord('A')
            a_inverse = inverse(a)
            new_num = a_inverse * (x - b) % 26
            plainText += chr((ord)('a') + new_num)

    return plainText

def main():
    print("Affine Cipher")  
	
    a = int(input("Enter a (coprime with 26): "))
    b = int(input("Enter b (0-25): "))

    boolean = coprime(a, b)

    if boolean == True:
        choice = int(input("\nEnter 1 to encrypt, 2 to decrypt: "))

        if choice == 1:
            cipherText = encrypt(a, b)
            print("\nCipher Text =", cipherText)

        elif choice == 2:
            plainText = decrypt(a, b)
            print("\nPlain Text =", plainText)
            
        else:
            print("Invalid Input")
    
    else:
        print("\nInvalid Input. Please try again.")
		
main()