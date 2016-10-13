//
//	Solution 4-4
//

class MyString
{
private:    
	char *data;
	int len;
	static int howmany;
	static int longest;
	
public:		
	// Constructor takes a char *
	// but if no arg then defaults to
	// empty string

	MyString(const char * = "" );
	
	~MyString();			   // Destructor
	int getLength();		   // Length 
	const char *getString();   // Get the string
	void reverse();			   // Reverse
	bool ispal();			   // Palindrome

	static int getCount();     // Number of strings
	static int getLongest();   // Length of longest string
};

