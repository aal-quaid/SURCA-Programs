#include <stdio.h>
#include <string.h>

#define SIZE 100
void encrypt(char alphabet_string[25]);//Function prototypes
void decrypt(char alphabet_string[25]);

int main(){
    int shift,choice;
    char alphabet_string[SIZE] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; //Sets letters equal to their place in the alphabet minus 1. E.g. A=0, Z=25
    printf("Caesar Cipher Program\n");
    printf("Enter 1 to encrypt a message\n");
    printf("Enter 2 to decrypt a message\n");
    scanf("%d",&choice);
    if(choice==1)
        encrypt(alphabet_string);
    else if (choice==2)
        decrypt(alphabet_string);
    else
        printf("Invalid Input\n"); //Validates input for choice. Can only be 1 or 2
    return 0;    
}

void encrypt(char alphabet_string[25]){
    char string[SIZE],encrypted[SIZE];
    int i,j;
    printf("Enter message to encrypt\n");
    scanf("%s",&string);
    for(i=0;i<strlen(string);i++){
        for(j=0;j<26;j++){
            if (string[i]==alphabet_string[j]){
                encrypted[i]=alphabet_string[(j+3)%26];
                break;//break statements end the nested loop when the correct letter has been found and added to the string 
            }
            else if (string[i]==(char)(((int)(alphabet_string[j])+32))){
                encrypted[i]=(char)((int)(alphabet_string[(j+3)%26])+32);//Checks for and adds a lowercase letter to the encrypted message 
                break;
            }
        }
    }
    printf("Encrypted Message: %s", encrypted);
}

void decrypt(char alphabet_string[25]){
    char string[SIZE],decrypted[SIZE];
    int i,j;
    printf("Enter message to decrypt\n");
    scanf("%s",&string);
    for(i=0;i<strlen(string);i++){
        for(j=0;j<26;j++){
            if (string[i]==alphabet_string[j]){
                decrypted[i]=alphabet_string[(j-3)%26];
                break;
            }
            else if (string[i]==(char)(((int)(alphabet_string[j])+32))){
                decrypted[i]=(char)((int)(alphabet_string[(j-3)%26])+32);//Checks for and adds a lowercase letter to the decrypted message 
                break;
            } 
        }
    }
    printf("Decrypted Message: %s", decrypted);
}
