#include <stdio.h>
#include <string.h>
#define SIZE 50//declares arbitrary size for string. Shouldn't be more than length 50 
void encrypt(char alphabet_string[25], int shift);//Function prototypes
void decrypt(char alphabet_string[25],int shift);

int main(){
    int shift,choice;
    char alphabet_string[SIZE] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; //Sets letters equal to their place in the alphabet minus 1. E.g. A=0, Z=25
    printf("Caesar Cipher Program\n");
    printf("Enter 1 to encrypt a message\n");
    printf("Enter 2 to decrypt a message\n");
    scanf("%d",&choice);
    printf("Enter shift\n");
    scanf("%d",&shift);
    if((shift>25)||(shift<1))
        printf("Invalid Input\n"); //Validates input for shift. Can't be greater than 25 or less than 1 
    if(choice==1)
        encrypt(alphabet_string,shift);
    else if (choice==2)
        decrypt(alphabet_string,shift);
    else
        printf("Invalid Input\n"); //Validates input for choice. Can only be 1 or 2
    return 0;    
}

void encrypt(char alphabet_string[25], int shift){
    char string[SIZE],encrypted[SIZE];
    int i,j;
    printf("Enter message to encrypt\n");
    scanf("%s",&string);
    for(i=0;i<strlen(string);i++){
        for(j=0;j<26;j++){
            if (string[i]==alphabet_string[j]){
                encrypted[i]=alphabet_string[(j+shift)%26];
                break;//break statements end the nested loop when the correct letter has been found and added to the string 
            }
            else if (string[i]==(char)(((int)(alphabet_string[j])+32))){
                encrypted[i]=(char)((int)(alphabet_string[(j+shift)%26])+32);//Checks for and adds a lowercase letter to the encrypted message 
                break;
            }   
        }
    }
    printf("Encrypted Message: %s", encrypted);
}

void decrypt(char alphabet_string[25], int shift){
    char string[SIZE],decrypted[SIZE];
    int i,j;
    printf("Enter message to decrypt\n");
    scanf("%s",&string);
    for(i=0;i<strlen(string);i++){
        for(j=0;j<26;j++){
            if (string[i]==alphabet_string[j]){
                decrypted[i]=alphabet_string[(j-shift)%26];
                break;
            }
            else if (string[i]==(char)(((int)(alphabet_string[j])+32))){
                decrypted[i]=(char)((int)(alphabet_string[(j-shift)%26])+32);//Checks for and adds a lowercase letter to the decrypted message 
                break;
            }   
        }
    }
    printf("Decrypted Message: %s", decrypted);
}
