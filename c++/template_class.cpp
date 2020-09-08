#include <iostream>
#include "base.h"

using  std::cout;
using std::endl;
using std::string;

/************** Template base *************/
template <class T>
class Accum{
    private:
        T total;
    public:
        Accum(T start):total(start){}
        T GetTotal() const {return total;}
        T operator+=(T const& t){total=total+t;return total;}
};

/************** Template Specilization for Person class *************/
template <>
class Accum<Person>{
    private:
        int total;
    public:
        Accum(int start):total(start){}
        int GetTotal() const {return total;}
        int operator+=(Person const& t){
            total = total + t.getMyNumber();
            return total;
        }
};

int main(){
    Accum<int> integers(0); //int is defining T type
    //Accum integers(0); //C++17 data type is not required
    integers +=3;
    integers +=7;
    cout<<"INTEGERS VALS "<<integers.GetTotal()<<endl;


    Accum<string> strings("");
    //Accum strings(string("")); //C++17 data type is not required
    strings +="Ankur";
    strings +=" ";
    strings +="Tanvi";
    cout<<"STRINGS VALS "<<strings.GetTotal()<<endl;

    Accum<Person> persons(0);
    Person p1(11);
    Person p2(111);
    persons += p1;
    persons += p2;
    cout<<"Persons VALS "<<persons.GetTotal()<<endl;
    return 0;
}