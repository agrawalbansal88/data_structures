#include <iostream>

using std::cout;
using std::endl;
using std::string;

int main(){
    int x =10;
    int *px=&x;
    *px = 11;
    cout<<"XXXX"<<x<<endl;

    int & py=x;
    py=12;
    cout<<"XXXX"<<x<<endl;
    return 0;
}
