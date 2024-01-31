#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //if there arent 2 argument counts, print this message
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    // if the argument entered is not a digit, print this message
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    //convert a string into an integer
    int k = atoi(argv[1]);

    //input plaintext, output the cipher text
    string plaintext = get_string("Plaintext: ");
    printf("Ciphertext: ");

    for (int j = 0; j < strlen(plaintext); j++)
    {
        //cipher using ASCI for uppercase letters
        if (isupper(plaintext[j]))
        {
            printf("%c", (plaintext[j] - 65 + k) % 26 + 65);
        }
        //cipher using ASCI for lowercase letters
        else if (islower(plaintext[j]))
        {
            printf("%c", (plaintext[j] - 97 + k) % 26 + 97);
        }
        else
        {
            printf("%c", plaintext[j]);
        }
    }
    printf("\n");
}