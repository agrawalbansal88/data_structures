#include<iostream> 
using namespace std; 

/* local variable is same as a member's name */
class Test 
{ 
private: 
int x; 
public: 
void setX (int x) 
{ 
	// The 'this' pointer is used to retrieve the object's x 
	// hidden by the local variable 'x' 
	this->x = x; 
} 
void print() { cout << "x = " << x << endl; } 
}; 

class StaticClass
{
    public:
    void print_val(){
        static int xx=10;
        xx++;
        printf("value of x=%d\n", xx);
    }
    int x; 
};

int main() 
{ 
    Test obj; 
    int x = 20; 
    obj.setX(x); 
    obj.print(); 

    StaticClass stat1;
    stat1.print_val();
    stat1.print_val();

    StaticClass stat2;
    stat2.print_val();
    stat2.print_val();
    return 0; 
} 

