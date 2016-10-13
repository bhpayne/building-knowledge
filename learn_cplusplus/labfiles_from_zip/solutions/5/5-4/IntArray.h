//
//	Solution for Exercise 5-4
//

class IntArray
{
private:    
	int howmany;
	int *data;
	
	void helper(const IntArray & car);
    void reinit(int val);

public:
	IntArray(int size = 10);
	IntArray(const IntArray & car);

	~IntArray();

	IntArray & operator=(const IntArray & car);
	IntArray & operator=(int value);
	int & operator[](int pos);
	IntArray & operator++();
	IntArray operator+(const IntArray & car);
	
    void reset(int val = 0);
	void print();
};



