//
//	3-11.cpp
//
#include <iostream>
double average(const int *data, int amount);
int main()
{
	const int howmany = 5;
	int x[ ] = { 10, 30, 115, -20, 11 };
	double result;
	result = average(x,howmany);
	std::cout << result << "\n";
	return 0;
}
double average(const int *data, int amount)
{
	double sum = 0.0; 
	int i;
	for ( i = 0; i < amount; i++)
		sum += data[i];
	return sum/amount;
}
