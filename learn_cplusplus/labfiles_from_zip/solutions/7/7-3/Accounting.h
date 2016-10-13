//
// Solution for Exercise 7-3
//

#ifndef ACCOUNTING_H
#define ACCOUNTING_H

#include "Contractor.h"

class Accounting : public Contractor
{
public:
	Accounting (string s);
	
	virtual double pay();
	virtual void vacation();
	virtual void review();
};
#endif
