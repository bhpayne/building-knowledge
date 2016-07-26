//
//	Stack.h
//
//	Template Stack class
//

template <class T>
class Stack {
    
private:    
	int sp;
	T *stack;
	
public:
	Stack(int size = 10);	
	void push(T & value);
	T pop();
	bool isEmpty();
};

