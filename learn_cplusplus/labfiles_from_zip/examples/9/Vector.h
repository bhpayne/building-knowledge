//
//  Vector.h
//

class Vector {
private:    
	int size;
	int maxValue;
	
	int *p;
	
public:
	Vector(int sz = 100, int max = 2000);

	int getValue(int pos);
	void setValue(int pos, int value);
};


