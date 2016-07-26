//
//	Solution 4-1
//

class MyDate
{
private:
	int day;
	int month;
	int year;
	
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
};


