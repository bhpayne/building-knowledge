//
// Starter for Exercise 7-3
//

#include "Worker.h"

int Worker::ids = 1;

Worker::Worker(string n)
{
	id = ids++;
	name = n;
}

int Worker::getId()
{
	return id;
}

string Worker::getName()
{
	return name;
}


