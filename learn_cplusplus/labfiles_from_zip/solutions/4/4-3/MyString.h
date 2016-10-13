//
//	Solution 4-3
//

class MyString
{
private:    
	char *data;
	int len;
	
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
};

