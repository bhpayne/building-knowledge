//
//
// 4-28.cpp
//
#include <iostream>
#include <string>

using namespace std;

class Test
{
private:    
    string value;
   
public:
    Test()
    {
       value = "empty";
       cout << value << endl;
    }
    
    Test(const char * v)
    {
       value = v;
       cout << "creating " << value << endl;
    }
    
    ~Test()
    { 
        cout << "destroying " << value << endl;
    }
 };
 
 void fun2()
 {  
    cout << "inside fun2()" << endl;
    Test t4("four");
    cout << "leaving fun2()" << endl;
 }
 
 void fun1()
 {  
    cout << "inside fun1()" << endl;
    Test t3("three");
    cout << "calling fun2()" << endl;
    fun2();
    cout << "leaving fun1()" << endl;
 }
 
 int main()
 {
    Test t1("one"), t2("two");
    cout << "calling fun1()" << endl;
    fun1();
    
    Test *pt = new Test("five");
    
    return 0;
 }
