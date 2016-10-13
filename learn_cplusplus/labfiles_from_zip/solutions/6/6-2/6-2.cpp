//
//	Solution for Exercise 6-2
//

#include <iostream>

using namespace std;

#include "MyDate.h"
#include "MyString.h"
#include "Employee.h"
#include "Company.h"

int main() 
{
	MyDate today;
	Company company(today, "/training/etc", 5);
	
	cout << company.getCompanyName() << endl;
	company.showInceptionDate();
	cout << "SIZE OF COMPANY: " << company.companySize() << endl;
	company.printWorkers();

	MyString ms1("mike");
	MyString ms2("susan");
	MyString ms3("erin");
	Employee e1(ms1, today);
	Employee e2(ms2, today);
	Employee e3(ms3, today);

	company.addEmployee(e1);
	company.addEmployee(e2);
	company.addEmployee(e3);
	
	cout << "SIZE OF COMPANY: " << company.companySize() << endl;	
	company.printWorkers();

	(*company.getEmployee(ms1)).print();
	
	return 0;
}
