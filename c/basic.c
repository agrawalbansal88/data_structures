#include <stdio.h>
#include<string.h>
#include <stdlib.h>

int doubeNumber(int x)
{
    int p;
    p = x*x;
    return p;
}

struct basic
{
    /* data */
    int c;
    float f;
    char stri[100];
};

void f1()
{
    printf("Ankur\n");
    int x =10;
    x= doubeNumber(x);
    printf("New value %d\n", x);

    struct basic ba;
    memset(ba.stri, 0, 100);
    strcpy(ba.stri,"d");
    printf("baisc.stri %c\n", ba.stri[0]);
    printf("baisc.stri %c\n", ba.stri[1]);

    char ch[20] ={'A', 'B', '\0'};
    printf("length of ch %s:%lu\n", ch, strlen(ch));
    char ch1[20] ={'A', 'B'};
    printf("length of ch1 %s:%lu\n", ch1, strlen(ch1));
}

void memory()
{
    int *ptr;
    int N=10;
    ptr =  (int*)malloc(N*sizeof(int));
    if (ptr == NULL){
        printf("Memory alloc failed");
    }
    else{
        for (int i =0;i <N;i++)
        {
            ptr[i] = i+1;
        }

        for (int i =0;i <N;i++)
        {
            printf("ptr[%d]=%d\n", i, ptr[i]);
        }
        free(ptr);
        ptr = NULL;
    }

}

void by_value(int x){
    x=10;
}
void by_ref(int* x){
    *x=10;
}

void call_by_value_by_ref(){
    
    int z=100;
    printf("before calling by value z=%d\n",z);
    by_value(z);
    printf("after calling by value z=%d\n",z);
    by_ref(&z);
    printf("after calling by ref z=%d\n",z);

}
void file_handling()
{
    FILE *f1;
    char dataToRead[50];
    f1= fopen("/Users/ankuragr/int_tests/c/sample.txt","rw");
    if (f1==NULL)
    {
        //could not open file
    }
    else
    {
         printf("FILE IS OPENED FOR READING\n");

        while (fgets(dataToRead, 50, f1) != NULL)
        {
            printf("READ data = %s\n\n", dataToRead);
        }
        fclose(f1);
    }
    
}
struct A
{
unsigned char c1 : 3;
unsigned char c2 : 4;
unsigned char c3 : 1;
}a;

struct B
{
unsigned char c1 : 3;
unsigned char : 0;
unsigned char c2 : 4;
unsigned char c3 : 1;
}b;
struct C
{
char c1;
int c2;
char c3[3];
}c;

void may_24()
{
    printf ("size of A %lu\n", sizeof(a));
    printf ("size of B %lu\n", sizeof(b));
    printf ("size of C %lu\n", sizeof(c));

 printf("\nab");
 printf("\bsi");
 printf("\rha");
    //printf("\n");
  int a=-2;
  printf("\n%x\n",a>>3);
  printf("\n%d\n",a>>3);
}
void ref( int *aa){
    *aa=11;
}
 
void pass_by_refrece(){
    int aa =10;
    int ba =20;

   ref(&aa);
    printf("value of a %d\n", aa);
    printf("value of b %d\n", ba);

}
#define CHECK_VAL(x) (x>0)
int main()
{
    //may_24();
    //f1();
    //memory();
    //call_by_value_by_ref();
    //file_handling();
    pass_by_refrece();
    printf("CHECK_VAL[%d]\n", CHECK_VAL(-10));
    return 0;
}
