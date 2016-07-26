//
//	9-10.cpp
//
#include <iostream>

using namespace std;

class Transport
{
protected:
	int x;
	
public:
	Transport() {}
	void carry() {}
};

class Plane : public Transport
{
public:
	Plane() {}
	void fly() {}
};

class Boat : public Transport
{
public:
	Boat() {}
	void motor() {}
};

class SeaPlane : public Plane, public Boat
{
public:
	SeaPlane()  { x = 0;}
};

int main()
{
	SeaPlane sp;
	sp.carry();
	
	return 0;
}
