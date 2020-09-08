#include <iostream>
#include "base.h"

using  std::cout;
using std::endl;

template <class T>
T max(T const& t1, T const& t2){
    return t1<t2?t2:t1;
}

int main(){
    Person p1(10);
    Person p2(11);
    cout << "MAX of 3 and 4 is " << max(3,4) << endl;
    cout << "MAX of 3 and 4 is " << max(p1,p2).getMyNumber() << endl;
    //count <<"MAX of Ankur and Tanvii is %s\n", max("Ankur","Tanvii") <<endl;
    return 0;
}