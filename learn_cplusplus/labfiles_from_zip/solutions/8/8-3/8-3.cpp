//
//	Solution 8-3.cpp
//
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

class Fraction
{
private:
	int n,d;
	
public:
	Fraction(int a = 0, int b = 1) : n(a), d(b) {}
	
	friend ostream & operator<<(ostream & os, const Fraction & cfr)
	{
		os << cfr.n << "/" << cfr.d << "\n";
		return os;
	}
};

int main(int argc, char ** argv)
{
	fstream f("ratios", ios::in | ios::ate);
	if ( ! f)  {
		cerr << "error opening ratios\n";
		exit(0);
	}
	
	long fileSize = f.tellg();
	int recs = fileSize / sizeof(Fraction);

	int rec_no;
	Fraction fr;
	int i = 1;
	
	while ( --argc > 0 )
	{
		rec_no = atoi(argv[i++]);
		if ( rec_no <= 0 || rec_no >= recs )
		{
			cerr << rec_no << " out of range " << endl;
			continue;
		}
		f.seekg(sizeof(Fraction) * (rec_no - 1));
		f.read((char *) & fr, sizeof(Fraction));
		cout << fr;
	}

	return 0;
}


