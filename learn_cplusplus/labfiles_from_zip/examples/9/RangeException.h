//
//  RangeException.h
//
		
class RangeException {
private:    
	int pos;
	char msg[100];
	
public:
	RangeException(int p, const char *m);
	
	int getPos();
	const char *getMsg();
};
		

