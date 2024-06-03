#include <stdio.h>
#include <string.h>

#define SIZE 100
void encrypt();//Function prototypes
void decrypt();

int main(){
    int choice;
    printf("Caesar Cipher Program\n");
    printf("Enter 1 to encrypt a message\n");
    printf("Enter 2 to decrypt a message\n");
    scanf("%d",&choice);
    if(choice==1)
        encrypt();
    else if (choice==2)
        decrypt();
    else
        printf("Invalid Input\n"); //Validates input for choice. Can only be 1 or 2
    return 0;    
}

void encrypt(){
    char string[SIZE],encrypted[SIZE];
    int i,num,new_num;
    printf("Enter message to encrypt\n");
    scanf("%s",&string);
    for(i=0;i<strlen(string);i++){
        num = (int)(string[i])-(int)('a');
        new_num = (num+3)%26;
        encrypted[i] = (char)((int)('A')+new_num);
    }
    printf("Encrypted Message: %s", encrypted);
}

void decrypt(char alphabet_string[25]){
    char string[SIZE],decrypted[SIZE];
    int i,num,new_num;
    printf("Enter message to decrypt\n");
    scanf("%s",&string);
    for(i=0;i<strlen(string);i++){
        num = (int)(string[i])-(int)('a');
        new_num = (num-3)%26;
        decrypted[i] = (char)((int)('A')+new_num);
    }
    printf("Decrypted Message: %s", decrypted);
}
