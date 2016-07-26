//
//	Fraction.h
//

class Fraction 
{
private:    
	int numer;
	int denom;
	
public:
	Fraction(int a = 0, int b = 1);
	
	void print();
	void recip();

	Fraction operator*(const Fraction & p);
	Fraction operator+(const Fraction & p);
	Fraction operator/(const Fraction & p);
	Fraction operator-(const Fraction & p);
};

