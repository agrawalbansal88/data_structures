
#include "base.h"
#include <iostream>

using namespace std;

int main(){
    Person p1(11);
    Person p2(12);
    if (p1<p2){
        printf("IS LESS\n");
    }
    GoodPerson gp1(22);
    gp1.setEnum1(Enum1::oneone);
    p1.setMyNumber(12);
    cout<<p1.getMyNumber()<<endl;
    return 0;
}
