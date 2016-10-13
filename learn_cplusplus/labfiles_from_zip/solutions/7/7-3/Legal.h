//
// Solution for Exercise 7-3
//

#ifndef LEGAL_H
#define LEGAL_H

#include "Contractor.h"

class Legal : public Contractor
{
public:
	Legal(string s);
	
	virtual double pay();
	virtual void vacation();
	virtual void review();
};

#endif

