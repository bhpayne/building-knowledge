//
//	Solution 6-2
//
#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

#include "MyDate.h"
#include "MyString.h"
#include "Employee.h"
#include "Company.h"

Company::Company(MyDate date, MyString name, int howmany)
{
    inception = date;
    companyName = name;
	capacity = howmany;
	workers = new Employee *[howmany];
	if (workers == 0) {
	    cerr << "Memory allocation failed in Company constructor" << endl;
	    exit(1);
	}
	numPeople = 0;
}

const char * Company::getCompanyName() const
{
	return companyName.getString();
}

int Company::companySize() const
{
	return numPeople;
}

void Company::showInceptionDate() const
{
	inception.print();
}

Employee * Company::getEmployee(MyString p)
{
	int i;
	for (i = 0; i < numPeople; i++) {
	   if (strcmp((*workers[i]).getName().getString(),p.getString())==0) 
		return workers[i];
	}
	return 0;
}

void Company::addEmployee(Employee & p)
{
	if ( numPeople < capacity )
		workers[numPeople++] = &p;
	else
		cout << "company not hiring any more" << endl;
}

void Company::printWorkers() const
{
	int i;
	for ( i = 0; i < numPeople; i++)
	{
		Employee e = (*workers[i]);
		e.print();
	}
}

