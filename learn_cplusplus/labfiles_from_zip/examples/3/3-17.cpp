//
//	3-17.cpp
//
#include <iostream>

int x = 1;
int & f( )
{
	return x;
}
main( )
{
	int y;
	y = f( ) + f( );		  // f( ) == x
	std::cout << y << "\n";   //  prints 2
	f( ) = y;				  //  x = 2
	std::cout << x << "\n";   //  prints 2
}

