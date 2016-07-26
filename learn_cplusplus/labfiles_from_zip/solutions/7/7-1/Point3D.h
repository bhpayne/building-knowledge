//
// Solution 7-1
//

#ifndef POINT3D_H
#define POINT3D_H

#include "Point.h"

class Point3D : public Point
{
protected:
	int z;
	
public:
	Point3D(int x, int y, int z);
	
	int getZ();
	
	void print();
};

#endif

