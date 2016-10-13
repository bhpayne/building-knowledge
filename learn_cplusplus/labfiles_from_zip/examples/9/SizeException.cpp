//
//  SizeException.cpp
//
#include <string.h>

#include "SizeException.h"

SizeException::SizeException(int v, const char *m)
{
	val = v;
	strcpy(msg, m);
}

int SizeException::getVal()
{
	return val;
}

const char * SizeException::getMsg()
{
	return msg;
}


