//
//	3-29.cpp
//
#include <iostream>
#include <string>
int main()
{
	std::string simple("must include");
	std::cout << simple << "\n"; 
	simple.append(" string");
	std::cout << simple << "\n";
	std::cout << simple.length() << "\n";
	std::cout << simple[0] << "\n";
	std::string phrase;
	phrase = simple;
	phrase.append(" to work. ");
	std::cout << simple << "\n";
	std::cout << phrase << "\n";
	return 0;
} 
