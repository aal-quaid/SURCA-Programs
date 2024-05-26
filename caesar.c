#include <stdio.h>
#include <string.h>

#define SIZE 100

void encryption(char plainText[]);

void decryption(char cipherText[]);

int main(){
    char plainText[SIZE], cipherText[SIZE];
    int choice;

    printf("Enter 0 to encrypt and 1 to decrypt:\n");
    scanf("%d", &choice);
    getchar();

    if(choice == 0){
        printf("Enter plain text:\n");
        fgets(plainText, sizeof(plainText), stdin);

        plainText[strcspn(plainText, "\n")] = 0;

        encryption(plainText);
    }

    else if(choice == 1){
        printf("Enter cipher text:\n");
        fgets(cipherText, sizeof(cipherText), stdin);

        cipherText[strcspn(cipherText, "\n")] = 0;

        decryption(cipherText);
    }

    else{
        printf("\nInvalid Input\n");
    }

    return 0;
}

void encryption(char plainText[]){
    char cipherText[SIZE] = "";
    char P, C;      //C = CipherText, P = plainText
    int i, length = strlen(plainText);

    strupr(plainText);

    for(i=0; i < length; i++){
        P = plainText[i];
        if(P == ' '){
            strncat(cipherText, &P, 1);
        }
        else{
            C = ((P - 65) + 3) % 26;
            C = C + 65;
            strncat(cipherText, &C, 1);
        }
    }

    printf("\nCipher Text = %s", cipherText);
}

void decryption(char cipherText[]){
    char plainText[SIZE] = "";
    char C, P;      // C = CipherText, P = plainText
    int i, length = strlen(cipherText);

    strlwr(cipherText);

    for(i=0; i < length; i++){
        C = cipherText[i];
        if(C == ' '){
            strncat(plainText, &C, 1);
        }
        else{
            P = ((C - 97) - 3) % 26;

            if(P < 0){
                P += 26;
                P = P + 97;
            }
            else{
                P = P % 26;
                P = P + 97;
            }
            strncat(plainText, &P, 1);
        }
    }

    printf("\nPlain Text = %s", plainText);
}