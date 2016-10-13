//
// Solution for Exercise 7-3
//

#ifndef CONTRACTOR_H
#define CONTRACTOR_H

#include "Worker.h"

class Contractor : public Worker
{
public:
	Contractor(string s);
	virtual void review() = 0;
};

#endif

