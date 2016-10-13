//
//	Solution 8-1
//
#include <iostream>
#include <string.h>			// strcpy, strlen, strcmp
#include <stdlib.h>			// exit

using namespace std;

#include "MyString.h"

MyString::MyString(const char *str)
{
	data = new char[(len = strlen(str)) + 1];
	if(data)
		strcpy(data,str);
	else
	{
		cout << "No memory\n";	
		exit(1);
	}
	
	howmany++;
	if ( len > longest)
		longest = len;
}

MyString::MyString(const MyString & cmsr)
{
	howmany++;
	len = cmsr.len;
	data = new char[len + 1];
	strcpy(data, cmsr.data);
}

MyString::~MyString()
{
	delete [] data;
	
	howmany--;
}

MyString & MyString::operator=(const MyString & cmsr)
{
	if ( this != &cmsr )
	{
		delete [] data;
		len = cmsr.len;
		data = new char[len + 1];
		strcpy(data, cmsr.data);
	}
	return *this;
}

bool MyString::operator==(const MyString & cmsr)
{
    return (strcmp(data, cmsr.data) == 0);
}

int MyString::getLength() const
{
	return len;
}

const char *MyString::getString() const
{ 
	return data;
}

void MyString::reverse() 
{
	int end = len - 1;
	char temp;
	for (int i = 0; i < end; i++)
	{
		temp = data[i];
		data[i] = data[end];
		data[end--] = temp;
	}
}

bool MyString::ispal() 
{
	MyString temp(data);
	temp.reverse();
	return(strcmp(data,temp.data) == 0);
}

int MyString::howmany = 0;
int MyString::longest = 0;

int MyString::getLongest()
{
	return longest;
}

int MyString::getCount()
{
	return howmany;
}

ostream & operator<<(ostream & os, const MyString & cmsr)
{
	os << cmsr.data;
	return os;
}

istream & operator>>(istream & is, MyString & cmsr)
{
	char line[1000];
	cin >> line;
	delete [] cmsr.data;
	cmsr.len = strlen(line);
	cmsr.data = new char[cmsr.len + 1];
	strcpy(cmsr.data, line);
	return is;
}
