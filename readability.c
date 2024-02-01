#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//prototype of letter count
int count_letters(string text);

int main(void)
{
    // User input text
    string text = get_string("Text: ");
    //Display copy of text
    printf("%s\n", text);

    int count_letters(string text);
    int letters = 0;
    // words begin at a 1 count because for every 1 space there are 2 words (logical)
    int words = 1;
    int sentences = 0;
    //counting letters, words, & sentences
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
        //counting spaces to count the words
        else if (text[i] == ' ')
        {
            words++;
        }
        //counting period, exclamation point, or question mark to indicate amount of sentences
        else if(text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    //calculating grade level
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;

    //equation for grade level rounded
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    //grade level below first
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    //grade level above 16
    else if(index > 16)
    {
        printf("Grade 16+\n");
    }
    //grade levels between 1 & 16
    else
    {
        printf("Grade %i\n", index);
    }
}