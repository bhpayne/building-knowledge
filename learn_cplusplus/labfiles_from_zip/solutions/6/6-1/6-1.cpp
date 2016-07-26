//
//	Solution 6-1
//
#include "MyDate.h"
#include "MyString.h"
#include "Employee.h"

int main()
{
	MyString name("Michael");
	MyDate today;
	Employee candidate(name, today);
	
	candidate.print();
	
	return 0;
}


