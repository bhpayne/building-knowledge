//
//	IntArray.h
//

class IntArray
{
private:    
	int howmany;
	int *data;
	
public:

	IntArray(int size = 10);                        // Constructor
	IntArray(const IntArray & car); 	            // Copy constructor

	IntArray & operator=(const IntArray & car); 	// Assignment Operator

	~IntArray();                                    // Destructor
	
	void print();
};


