//
// Solution 7-1
//

#ifndef POINT_H
#define POINT_H

class Point
{
protected:
	int n, d;
	
public:
	Point(int a = 0, int b = 1);
	
	int getX();
	int getY();
	
	void print();
};

#endif

