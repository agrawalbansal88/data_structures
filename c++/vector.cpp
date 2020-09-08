# include <iostream>
# include <vector>
#include <list>

using  std::cout;
using  std::endl;
using  std::vector;
using std::list;

void set1(){
    vector<int> numbers;
    //v.push_back(num) at entry at last
    //v.at(index) return value at index 
    //v.begin() --reads vector from index 0
    //v.size() size of vector
    //v.capacity() OS allocate more then size so that it will not have to get new memory for an insert
    //v.shrink_to_fit() that will make size and capacity as same
    //v.insert(location, value), -- insert before location
    //v.earse(location)
    //v.clear() // remove all elements
    //v.empty()--- retrun bool true if empty
    //v.data() returnd data which we can use a pointer
    //v.

    numbers.push_back(11);
    numbers.push_back(12);
    for (int i =0;i<numbers.size();i++){
        cout<<i<<"A "<<numbers[i]<<endl;
    }
    numbers.insert(numbers.begin()+1, 10);
    for (int i =0;i<numbers.size();i++){
        cout<<i<<" B   "<<numbers[i]<<endl;
    }
    numbers.erase(numbers.begin()+1);
    for (int i =0;i<numbers.size();i++){
        cout<<i<<"    C    "<<numbers[i]<<endl;
    }
    //cout<<" D "<<numbers.empty()<<endl;
    numbers.clear();
    for (int i =0;i<numbers.size();i++){
        cout<<i<<" E "<<numbers[i]<<endl;
    }
    cout<<"F  "<<numbers.empty()<<endl;

    //using iterator
    for (vector<int>::iterator i =numbers.begin();i != numbers.end();i++){
        cout<<" E "<<*i<<endl;
    }
}

void fillV(vector<int>& v){
    v.push_back(11);
    v.push_back(1);
    v.push_back(11);
    v.push_back(1111);
    v.pop_back();
    //cout<<"POpped "<<i<<endl;
}

void printVector(const vector<int>& v){
    
    cout<<"PRINTING V"<<endl;
    for (int i =0;i<v.size();i++){
        cout<<v[i]<<endl;
    }
}

void set2(){
    vector<int> myV;
    fillV(myV);
    printVector(myV);
}

void listSet(){
    // this is  doube link list
    list<double> l = {1,2,3,4,5};
    l.push_back(6);
    l.push_front(0.5);
    //l.reverse()
    //l.sort()
    //

    //print
    for (list<double>::iterator i =l.begin(); i != l.end(); i++){
        cout<<" E "<<*i<<endl;
    }
    l.pop_back();
    l.pop_front();

    cout<<"front "<<l.front()<<endl;
    cout<<"back "<<l.back()<<endl;
    cout<<l.size()<<endl;
}

int main(){
    //set1();
    //set2();
    listSet();
    return 0;
}
