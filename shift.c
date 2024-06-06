/* Assumption: 
plaintext - lowercase letters only
ciphertext - UPPER CASE LETTERS ONLY
*/
#include <stdio.h>
#include <string.h>
#define SIZE 100

void encryption(char plainText[], int shift);
void decryption(char cipherText[], int shift);

int main(){
    char string[SIZE];
    int choice = 1, shift;

    while(choice != 0){
        printf("Enter 1 to encrypt, 2 to decrypt, and 0 to exit:\n");
        scanf("%d", &choice);
        getchar();

        if(choice == 1){
            printf("Enter Shift:\n");
            scanf("%d", &shift);
            getchar();
            
            printf("Enter plain text:\n");
            fgets(string, sizeof(string), stdin);           // gets the whole string including spaces

            string[strcspn(string, "\n")] = 0;              // Removes '\n' from the string

            encryption(string, shift);   
        }

        else if(choice == 2){
            printf("Enter Shift:\n");
            scanf("%d", &shift);
            getchar();

            printf("Enter cipher text:\n");
            fgets(string, sizeof(string), stdin);           // gets the whole string including spaces

            string[strcspn(string, "\n")] = 0;              // Removes '\n' from the string

            decryption(string, shift);
        }
    }
    printf("\nGood Bye!\n");

    return 0;
}

void encryption(char plainText[], int shift){
    char cipherText[SIZE];
    char P, C;
    int i, length = strlen(plainText);

    for(i=0; i < length; i++){
        P = plainText[i];
        if(P == ' '){
            cipherText[i] = ' ';
        }
        else{
            C = ((P - (int)('a')) + shift) % 26;
            C = C + (int)('A');
            cipherText[i] = C;
        }
    }
    cipherText[i] = '\0';

    printf("\nCipher Text = %s\n", cipherText);
}

void decryption(char cipherText[], int shift){
    char plainText[SIZE];
    char C, P;
    int i, length = strlen(cipherText);

    for(i=0; i < length; i++){
        C = cipherText[i];

        if(C == ' '){
            plainText[i] = ' ';
        }
        else{
            P = ((C - (int)('A')) - shift);

            if(P < 0){
                P += 26 + (int)('a');
            }
            else{
                P = (P % 26) + (int)('a');
            }
            plainText[i] = P;
        }
    }
    plainText[i] = '\0';

    printf("\nPlain Text = %s\n", plainText);
}