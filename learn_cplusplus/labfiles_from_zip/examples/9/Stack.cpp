//
//	Stack.cpp
//
//	Template Stack class
//

#include "Stack.h"

template <class T>
Stack<T>::Stack(int size )
{	
	stack = new T[size];
	sp = 0;
}

template <class T>
void Stack<T>::push(T & value)
{
	stack[sp++]  = value;
}

template <class T> T Stack<T>::pop( )
{
	return(stack[--sp]);
}

template <class T>
bool Stack<T>::isEmpty()
{
	return sp == 0;
}

