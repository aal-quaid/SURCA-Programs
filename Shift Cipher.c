#include <stdio.h>
#include <string.h>

#define SIZE 100
void encrypt(int shift);//Function prototypes
void decrypt(int shift);

int main(){
    int choice,shift;
    printf("Shift Cipher Program\n");
    printf("Enter shift:\n");
    scanf("%d",&shift);
    printf("Enter 1 to encrypt a message\n");
    printf("Enter 2 to decrypt a message\n");
    scanf("%d",&choice);
    if(choice==1)
        encrypt(shift);
    else if (choice==2)
        decrypt(shift);
    else
        printf("Invalid Input\n"); //Validates input for choice. Can only be 1 or 2
    return 0;    
}

void encrypt(int shift){
    char string[SIZE],encrypted[SIZE];
    int i,num,new_num;
    printf("Enter message to encrypt\n");
    scanf("%s",&string);
    for(i=0;i<strlen(string);i++){
        num = (int)(string[i])-(int)('a');
        new_num = (num+shift)%26;
        encrypted[i] = (char)((int)('A')+new_num);
    }
    printf("Encrypted Message: %s", encrypted);
}

void decrypt(int shift){
    char string[SIZE],decrypted[SIZE];
    int i,num,new_num;
    printf("Enter message to decrypt\n");
    scanf("%s",&string);
    for(i=0;i<strlen(string);i++){
        if((int)(string[i])-(int)('a')>0){
        num = (int)(string[i])-(int)('a');
        new_num = (num-shift)%26;
        decrypted[i] = (char)((int)('A')+new_num);
        }
        else if((int)(string[i])-(int)('a')<0){
            num = (int)(string[i])-(int)('a');
            new_num = ((num-shift)*-1);
            decrypted[i] = (char)((int)('A')+new_num); 
        }
        else{
            decrypted[i] =(int)('Z')-(shift-1); 
        }
    }
    printf("Decrypted Message: %s", decrypted);
}
