#include<stdio.h>

int main(void)
{
    int i = 6, j = 4, k;
    k = ++i * --j;
    printf("%d\n", k);

    i = 6;
    j = 4;

    k = i++ * j--;
    printf("%d\n", k);
}