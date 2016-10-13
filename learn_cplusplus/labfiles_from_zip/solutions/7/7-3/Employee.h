//
// Solution for Exercise 7-3
//

#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include "Worker.h"

class Employee : public Worker
{
public:
	Employee(string s);
	
	virtual double pension() = 0;
	virtual void bonus() = 0;
};

#endif

