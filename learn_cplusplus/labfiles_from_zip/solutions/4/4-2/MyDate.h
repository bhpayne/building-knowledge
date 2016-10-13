//
//	Solution 4-2
//
#include <string>

using namespace std;

class MyDate
{
private:
	int day;
	int month;
	int year;
	static string months[13];
	static int days[12];
	
	void help(int a, int b, int c);
	
public:
	MyDate(int d, int m, int y);
	MyDate(int d, int m);
	MyDate(int d);
	MyDate();

	void print();
	int getDay();
	int getMonth();
	int getYear();

	string getMonthAsString();
	int getDayOfYear();
};


