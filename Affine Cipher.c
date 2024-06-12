#include <stdio.h>
#include <string.h>

#define SIZE 100

void encrypt(int shift, int multiplier); //Function prototypes
void decrypt(int shift, int multiplier);
int coprime(int multiplier);
int modInverse(int multiplier);

int main(){
    int shift, multiplier, choice, isCoprime;
    printf("Affine Cipher Program\n");
    printf("Enter shift: ");
    scanf("%d",&shift);
    printf("\n");
    printf("Enter multiplier: ");
    scanf("%d",&multiplier);
    printf("\n");
    isCoprime = coprime(multiplier);
    if (isCoprime==1){
        printf("Enter 1 to encrypt a message, enter 2 to decrypt a message: ");
        scanf("%d",&choice);
        printf("\n");
        if (choice==1)
            encrypt(shift, multiplier);
        else if (choice==2)
            decrypt(shift,multiplier);
        else
            printf("Invalid input. Please try again."); //Validates Input
    }
    else{
        printf("Multiplier must be coprime with 26. Please try again."); //Multiplier must be coprime with 26 to properly encrypt/decrypt
    }
    return 0;
}

int coprime(int multiplier){
    int a=multiplier, b=26,x;
    if (26<=multiplier)
        return -1;

    while (a>0){
        x = b % a;
        b = a;
        a = x;
    }
    if (b>1 && a==0)
        return -1;
    else
        return 1;
}

void encrypt(int shift, int multiplier){
    char plainText[SIZE], encrypted[SIZE];
    int i,tempVar;
    printf("Enter message to encrypt: ");
    scanf(" %[^\n]s", plainText); //Takes input with spaces
    printf("\n");
    for(i=0;i<strlen(plainText);i++){
        if((int)(plainText[i])>=65&&(int)(plainText[i])<=90){ //uppercase ASCII values
            tempVar = (int)(plainText[i]) - (int)('A'); //uses ASCII values to set letters to values 0-25
            encrypted[i] = (char)((int)('A')+((multiplier*tempVar)+shift)%26);
        }
        else if((int)(plainText[i])>=97&&(int)(plainText[i])<=122){ //lowercase ASCII values
            tempVar = (int)(plainText[i]) - (int)('a');
            encrypted[i] = (char)((int)('a')+((multiplier*tempVar)+shift)%26);
        }
        else{
            encrypted[i] = plainText[i]; //adds any non-alphabetic characters back into the encrypted message
        }
    }
    printf("Encrypted Message: %s",encrypted);
}

void decrypt(int shift, int multiplier){
    char plainText[SIZE], decrypted[SIZE];
    int i,tempVar,a;
    a = modInverse(multiplier);
    printf("Enter message to decrypt: ");
    scanf(" %[^\n]s", plainText);
    printf("\n");
    for(i=0;i<strlen(plainText);i++){
        if((int)(plainText[i])>=65&&(int)(plainText[i])<=90){
            tempVar = (int)(plainText[i])-(int)('A'); 
            decrypted[i] = (char)((int)('A')+(a*(tempVar-shift+26)%26));
        }
        else if ((int)(plainText[i])>=97&&(int)(plainText[i])<=122){
            tempVar = (int)(plainText[i])-(int)('a'); 
            decrypted[i] = (char)((int)('a')+(a*(tempVar-shift+26)%26));
        }
        else{
            decrypted[i] = plainText[i];
        }
    }
    printf("Decrypted Message: %s",decrypted); 
}

int modInverse(int multiplier){
    for(int i;i<26;i++){  
        if (((multiplier % 26) * (i % 26)) % 26 == 1)
            return i;
    }
    return -1;
}