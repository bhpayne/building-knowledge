//
//  SizeException.h
//
		
class SizeException
{
private:
	int val;
	char msg[100];
	
public:
	SizeException(int v, const char *m);
	
	int getVal();
	const char *getMsg();
};

