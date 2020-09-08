#pragma once

enum class Enum1{
    oneone,
    twotwo
};
enum class Enum2{
    oneone,
    twotwo
};

class Person
{
    private:
    int myNumber;
    friend bool operator<(Person const& p, int const& value);

    public:
    int getMyNumber() const;
    void setMyNumber(int);
    Person(int);
    Person();
    ~Person();
    bool operator<(Person const& p) const;
    bool operator<(int const value);
};

class GoodPerson: public Person
{
    private:
        Enum1 enum1;
    public:
    Enum1 getEnum1();
    void setEnum1(Enum1);
    GoodPerson(int);
};

Enum1 GoodPerson::getEnum1(){
    return enum1;
}

void GoodPerson::setEnum1(Enum1 number){
    enum1 = number;
}

GoodPerson::GoodPerson(int number): Person(number){
}

Person::Person(int number): myNumber(number){
}


Person::~Person(){
}
int Person::getMyNumber() const{
    return myNumber;
}

void Person::setMyNumber(int number){
    myNumber = number;
}

bool Person::operator<(Person const& p) const{
    return myNumber<p.myNumber;
}

bool Person::operator<(int const value){
    return myNumber<value;
}

bool operator<(Person const& p, int const& value){
    return p.myNumber<value;
}