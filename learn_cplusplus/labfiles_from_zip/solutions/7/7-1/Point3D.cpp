//
// Solution 7-1
//
#include <iostream>

using namespace std;

#include "Point3D.h"

Point3D::Point3D(int x, int y, int z) : Point(x,y)
{
	this->z = z;
}

int Point3D::getZ()
{
	return z;
}

void Point3D::print()
{
	Point::print();
	cout << "," << z;
}

