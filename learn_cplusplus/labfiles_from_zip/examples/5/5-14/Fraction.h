//
//	Fraction.h
//

class Fraction 
{
private:
	int numer;
	int denom;

public:
	Fraction(int n = 0, int d = 1);
	
	void recip();
	void print();

	friend Fraction operator*(const Fraction & p, const Fraction &);
	friend Fraction operator/(const Fraction & p, const Fraction &);
};


