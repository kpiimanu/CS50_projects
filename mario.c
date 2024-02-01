#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height, i, j, space;
    do
    //input height from user
    {
        height = get_int("Enter height of pyramid: ");
    }
    //ensure user inputs a value between 1 & 8
    while (height < 1 || height > 8);

    //rows of pyramid
    for (i = 0; i < height; i++)
    {
        //space in relation to height
        for (space = 0; space < height - i - 1; space++)
        {
            printf(" ");
        }
        //columns of pyramid
        for (j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}