//
//  Point.h
//

#ifndef POINT_H
#define POINT_H

#include <iostream>

using namespace std;

class Point 
{
private:    
	int xc, yc;
	
public:
	Point(int x, int y);
	Point(const Point & p);
	
	void print( ) const;
	
	Point & operator=(const Point &);
};

#endif

