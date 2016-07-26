//
//  RangeException.cpp
//
#include <string.h>

#include "RangeException.h"

RangeException::RangeException(int p, const char *m)
{
	pos = p;
	strcpy(msg, m);
}

int RangeException::getPos()
{
	return pos;
}

const char * RangeException::getMsg()
{
	return msg;
}



		

