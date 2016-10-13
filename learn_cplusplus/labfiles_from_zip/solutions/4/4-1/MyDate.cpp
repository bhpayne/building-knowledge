//
//	Solution 4-1
//
#include <iostream>
#include <time.h>

using namespace std;

#include "MyDate.h"

MyDate::MyDate(int d, int m, int y)
{
	help(d,m,y);
}

MyDate::MyDate(int d, int m)
{
	long int clock;
	time(&clock);
	struct tm *pt;
	pt = localtime(&clock);
	help(d, m, pt->tm_year + 1900);
}

MyDate::MyDate(int d)
{
	long int clock;
	time(&clock);
	struct tm *pt;
	pt = localtime(&clock);
	help(d, pt->tm_mon + 1, pt->tm_year + 1900);
}

MyDate::MyDate()
{
	long int clock;
	time(&clock);
	struct tm *pt;
	pt = localtime(&clock);
	help(pt->tm_mday, pt->tm_mon + 1, pt->tm_year + 1900);
}

void MyDate::help(int a, int b, int c)
{
	day = a;
	month = b;
	year = c;
}

void MyDate::print()
{
	cout << month << "/" << day << "/" << year << endl;
}

int MyDate::getDay()
{
	return day;
}

int MyDate::getMonth()
{
	return month;
}

int MyDate::getYear()
{
	return year;
}

