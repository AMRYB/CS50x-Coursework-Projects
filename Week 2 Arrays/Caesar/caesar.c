#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

string scramble_text(string plaintext, int key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        for (int i = 0, len = strlen(argv[1]); i < len; i++)
        {
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
    }

    string plaintext = get_string("Plaintext: ");
    int key = atoi(argv[1]);
    printf("Ciphertext: %s\n", scramble_text(plaintext, key));
}

string scramble_text(string plaintext, int key)
{
    string ciphertext = plaintext;
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        if (isupper(plaintext[i]))
        {
            ciphertext[i] = (plaintext[i] - 'A' + key) % 26 + 'A';
        }
        else if (islower(plaintext[i]))
        {
            ciphertext[i] = (plaintext[i] - 'a' + key) % 26 + 'a';
        }
    }
    return ciphertext;
}
