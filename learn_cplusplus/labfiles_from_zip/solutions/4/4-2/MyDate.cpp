//
//	Solution 4-2
//
#include <iostream>
#include <string>
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

string MyDate::months[] = 
{	"", "Jan", "Feb", "Mar", "Apr", "May", "June",
	"July", "Aug", "Sept", "Oct", "Nov", "Dec"
};
	
int MyDate::days[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

string MyDate::getMonthAsString()
{
	return months[month];
}

int MyDate::getDayOfYear()
{
	int total = 0;
	int i;
	for ( i = 0; i < month - 1; i++)
		total += days[i];
	return total + day;
}	
