/* Assumption: 
plaintext - lowercase letters only
ciphertext - UPPER CASE LETTERS ONLY
*/
#include <stdio.h>
#include <string.h>
#define SIZE 100

void encryption(int shift);     //Function Prototypes
void decryption(int shift);

int main(){
    int choice = 1, shift;

    printf("Shift Cipher Program\n");

    while(choice != 0){
        printf("Enter 1 to encrypt, 2 to decrypt, and 0 to exit:\n");
        scanf("%d", &choice);
        getchar();

        if(choice == 1){
            printf("Enter Shift:\n");
            scanf("%d", &shift);
            getchar();

            encryption(shift);   
        }
        else if(choice == 2){
            printf("Enter Shift:\n");
            scanf("%d", &shift);
            getchar();

            decryption(shift);
        }
    }
    printf("\nGood Bye!\n");

    return 0;
}

void encryption(int shift){
    char string[SIZE], encrypted[SIZE];
    int i, num, new_num;

    printf("Enter message to encrypt:\n");
    fgets(string, sizeof(string), stdin);           // gets the whole string including spaces

    string[strcspn(string, "\n")] = 0;              // Removes '\n' from the string

    for(i=0; i < strlen(string); i++){
        if(string[i] == ' '){
            encrypted[i] = ' ';                     // Adds spaces to the encrypted message
        }
        else{
            num = (int)(string[i]) - (int)('a');
            new_num = (num + shift) % 26;
            encrypted[i] = (char)((int)('A') + new_num); 
        }
    }
    printf("\nEncrypted Message = %s\n", encrypted);
}

void decryption(int shift){
    char string[SIZE], decrypted[SIZE];
    int i, num, new_num;

    printf("Enter message to decrypt:\n");
    fgets(string, sizeof(string), stdin);           // gets the whole string including spaces

    string[strcspn(string, "\n")] = 0;              // Removes '\n' from the string

    for(i=0; i < strlen(string); i++){

        if(string[i] == ' '){
            decrypted[i] = ' ';                     // Adds spaces to the decrypted message
        }
        else{
            num = (int)(string[i]) - (int)('A');
            
            if(num - shift < 0){
                new_num = (num - shift) + 26;       // C can't mod negative numbers, so we are adding 26 instead
                decrypted[i] = (char)((int)('a') + new_num);
            }
            else{
                new_num = ((num - shift) % 26);
                decrypted[i] = (char)((int)('a') + new_num); 
            }
        }
    }
    printf("\nDecrypted Message = %s\n", decrypted);
}