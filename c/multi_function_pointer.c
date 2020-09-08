
#include <stdio.h>
int dummy(int a, int b){
    printf("dummy called\n");
    return 0;
}
int add(int a, int b){
    printf("A+B called\n");
    return a+b;
}
int sub(int a, int b){
    printf("A-B called\n");
    return a-b;
}

int mul(int a, int b){
    printf("A*B called\n");
    return a*b;
}
int div(int a, int b){
    printf("A/B called\n");
    return a/b;
}

int (*pf[])(int,int) = {dummy,add, sub, mul, div};

int main(){

    for(int i=0;i<5;i++){
        int retval = pf[i](3,4);
        printf("retval =%d\n\n", retval);
    }

return 0;

}
