#include <stdio.h>

int Add(int a, int b)
{
    return a+b;
}

int main()
{
    printf("IN MAIN\n");

    int (*ptr)(int, int);
    ptr = Add;
    int c =  ptr(3,4);
    printf("value of C=%d\n", c);
}
