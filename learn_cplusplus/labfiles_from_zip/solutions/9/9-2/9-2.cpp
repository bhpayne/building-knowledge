//
//	Solution 9-2
//

#include <iostream>

using namespace std;

class Fraction {
private:    
	int numer;
	int denom;
	
public:
	friend Fraction operator+(const Fraction & f, const Fraction & s);

	Fraction(int a = 0, int b = 1)
	{
		numer = a;
		denom = b;
	}
	
	int operator<(const Fraction & f)
	{
		double d1 = (double) f.numer / f.denom;
		double d2 = (double) numer / denom;
		return d1 > d2 ? 1 : 0;
	}
	
	int operator!=(const Fraction & f)
	{
		return numer * f.denom == denom * f.numer;
	}
	
	friend ostream & operator<<(ostream & os, const Fraction & f);
};

ostream & operator<<(ostream & os, const Fraction & f)
{
	cout << f.numer << "/" << f.denom;
	return os;
}

Fraction operator+(const Fraction & f, const Fraction & s)
{
	Fraction temp;
	temp.numer = f.numer * s.denom + f.denom * s.numer;
	temp.denom = f.denom * s.denom;
	return temp;
}

template <class TYPE>
TYPE minimum(TYPE & a, TYPE & b)
{
	return a < b ? a : b;
}

template <class TYPE>
class Array {
private:    
	int howmany;
	TYPE *data;
	
public:
	Array(int size = 10)			// int constructor
	{
		howmany = size;
		data = new TYPE[howmany];
		int i;
		for (i = 0; i < howmany; i++)
			data[i] = 0;
	}
	
	Array(const Array & car)		// copy constructor
	{
		howmany = car.howmany;
		data = new TYPE[howmany];
		int i;
		for ( i = 0; i < howmany; i++)
			data[i] = car.data[i];
	}

	void print()				// print the array
	{
		cout << "[";
		int i;
		for (i = 0; i < howmany - 1; i++)
			cout << data[i] << ", ";
		cout << data[i];
		cout << "]" << endl;
	}
	
	int grow(int increase)			// increase size of array
	{
		Array temp(*this);
		delete [ ] data;
		howmany = temp.howmany + increase;
		data = new TYPE[howmany];
		int i;
		for (i = 0; i < temp.howmany; i++)
			data[i] = temp.data[i];
		while(i < howmany)
			data[i++] = 0;
		return howmany;
    }
  
	TYPE sum()				// compute sum of array elements
	{
		TYPE tot = 0;
		int i;
		for (i = 0; i < howmany; i++)
			tot = tot + data[i];
		return tot;
	}
	
	Array & operator=(const Array & car)	// assign one array to another
	{
        if ( this != & car)
        {
		    delete [ ] data;
		    howmany = car.howmany;
            data = new TYPE[howmany];
			int i;
			for(i = 0; i < howmany; i++)
				data[i] = car.data[i];
        }
	    return *this;
	}

	Array & operator=(TYPE value)		// assign int to each array[i]
	{
		int i;
		for(i = 0; i < howmany; i++)
			data[i] = value;
        return *this;
	}
	
	Array operator+(const Array & car)	// add 2 arrays
	{
		Array temp(car.howmany);
		int i;
		for (i = 0; i < car.howmany; i++)
			temp.data[i] = data[i] + car.data[i];
		return temp;
	}

	TYPE & operator[](int pos)		//subscript operator
	{
		if ( pos < 0 || pos >= howmany)
		{
			cout << "illegal sub " << pos << endl;
			return data[0];
		}
		else
			return data[pos];
	}
	
	int operator==(const Array & car)	// see if two arrays are equal
	{
		int i;
		for (i = 0; i < howmany; i++)
			if ( data[i] != car.data[i])
				return 0;
		return 1;
    }
        
	int operator!=(const Array & car)	// see if they are unequal
	{
		return ! (*this == car);
	}
};

int main()
{
	Array <int> x(10);
	x.print();
	x = 1;
	x.print();

	Array <Fraction> f(10);
	f.print();
	cout << f.sum() << endl;

	return 0;
}

