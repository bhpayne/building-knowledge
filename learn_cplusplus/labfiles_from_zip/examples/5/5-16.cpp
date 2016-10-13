//
//	5-16.cpp
//
#include <iostream>
#include <string>

using namespace std;

class Pair
{
private:
	int number;
	string name;
	
public:
	Pair(int number, string name)
	{
		cout << "creating " << name << endl;
		this -> number = number;
		this -> name = name;
	}
	
	~Pair()
	{
		cout << "destroying " << name << endl;
	}
};

void fun1(Pair param)
{

}

Pair fun2()
{
	Pair p2(200, "Joel");
	return p2;
}

int main()
{
	Pair p1(100, "Michael");
	Pair p2 = p1;
	fun1(p1);
	p1 = fun2();
	
	return 0;
}
		
