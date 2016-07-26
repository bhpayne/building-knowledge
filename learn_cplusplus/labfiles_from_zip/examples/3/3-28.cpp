//
//   3-28.cpp
//
#
#include <iostream>
bool isBigger(int p1, int p2)
{
	return p1 > p2;
}
int main()
{
	int x, y;
	std::cout << "enter two integers ";
	std::cin >> x >> y;
	bool isGreater = x > y;
	if ( isGreater )
		std::cout << x << " gt " << y << "\n";
	isGreater = isBigger(x, y);
	if ( isGreater )
		std::cout << isGreater << "\n";
	return 0;
}


