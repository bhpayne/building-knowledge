//
// Solution 7-1
//

#include <iostream>

using namespace std;

#include "Point.h"
#include "Point3D.h"

int main()
{
	Point  	p1(0,1);
	Point3D	p2(2,3,4);
	
	cout << p1.getX() << "," << p1.getY() << endl;
	cout << p2.getX() << "," << p2.getY() << "," << p2.getZ() << endl;
	
	p1.print();
	cout << endl;
	
	p2.print();
	cout << endl;
	
	return 0;
}


