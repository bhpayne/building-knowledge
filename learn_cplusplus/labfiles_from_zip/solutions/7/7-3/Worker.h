//
// Solution for Exercise 7-3
//

#ifndef WORKER_H
#define WORKER_H

#include <iostream>
#include <string>

using namespace std;

class Worker
{
	static int ids;
	int id;
	string name;
	
public:
	Worker(string);
	
	int getId();
	string getName();
	virtual double pay() = 0;
	virtual void vacation() = 0;
};
#endif
