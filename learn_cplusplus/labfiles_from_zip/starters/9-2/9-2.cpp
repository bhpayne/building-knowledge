//
//	Starter code for Exercise 9-2
//

#include <iostream>

using namespace std;

class Array {
private:    
	int howmany;
	int *data;
	
public:
	Array(int size = 10)			// int constructor
	{
		howmany = size;
		data = new int[howmany];
		int i;
		for (i = 0; i < howmany; i++)
			data[i] = 0;
	}
	
	Array(const Array & car)		// copy constructor
	{
		howmany = car.howmany;
		data = new int[howmany];
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
		data = new int[howmany];
		int i;
		for (i = 0; i < temp.howmany; i++)
			data[i] = temp.data[i];
		while(i < howmany)
			data[i++] = 0;
		return howmany;
    }
    
    int sum()				// compute sum of array elements
	{
        int tot = 0;
		int i;
		for (i = 0; i < howmany; i++)
			tot += data[i];
		return tot;
	}
	
	Array & operator=(const Array & car)	// assign one Array to another
	{
        if ( this != & car)
        {
			delete [ ] data;
			howmany = car.howmany;
            data = new int[howmany];
			int i;
			for(i = 0; i < howmany; i++)
				data[i] = car.data[i];
        }
	    return *this;
	}

	Array & operator=(int value)		// assign int to each array[i] 
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

	int & operator[](int pos)		//subscript operator
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
	Array x(10);
	x.print();
	x = 1;
	x.print();
	
	Array z(10);
	z = 2;
	
	Array c(10);
	c = x + z;
	c.print();
	x = c;
	x.print();
	cout << c.sum() << endl;
	
	int i;
	for ( i = 0; i < 10; i++)
		x[i] = i + 10;
		
	x.print();
	
	for ( i = 0; i <= 10; i++)
		cout << "x at [ " << i << " ] is " << x[i] << endl;
		
	x.print();
	
	Array r(10);
	Array s(10);
	Array t(10);
	t = 2;
	if ( r == s)
		cout << "EQUAL" << endl;
	if ( r != t)
        cout << "NOT EQUAL" << endl;
	c.grow(5);
	c.print();
	
	return 0;
}


