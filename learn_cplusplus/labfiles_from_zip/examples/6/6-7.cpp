//
//  6-7.cpp
//

#include "Point.h"
#include "Line.h"

int main()
{
	Point p1(0,0), p2(3,4);
	Line line1(p1, p2);
	Line line2 = line1;
	
	line1.print();
	line2.print();
	
	line1 = line2;
	
	return 0;
}
