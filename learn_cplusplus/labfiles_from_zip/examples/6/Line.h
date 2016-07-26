//
//  Line.h
//

#ifndef LINE_H
#define LINE_H

#include "Point.h"

class Line
{
private:    
	Point p1, p2;
	
public:
	Line(const Point & p1, const Point & p2);
	Line(const Line & clr);
	
	void print( ) const;

	Line & operator=(const Line & clr);
};

#endif
