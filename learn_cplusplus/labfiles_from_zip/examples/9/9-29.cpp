//
//  9-29.cpp
//

#include <iostream>
#include <cstdlib>

using namespace std;

#include "Vector.h"
#include "SizeException.h"
#include "RangeException.h"

int main()
{
	try
	{
		Vector x(10, 2000);
		
        int i;
        for (i = 0; i < 10; i++)
			x.setValue(i, i + 10);
			
		//
		// TRY DIFFERENT VALUES FOR THE NEXT TWO 
		// STATEMENTS SO THAT EACH EXCEPTION WILL BE THROWN
		//
			
		x.setValue(8,50);
		x.setValue(5,90);
		
		for (i = 0; i < 10; i++)
			cout << x.getValue(i) << endl;
	}
	catch (RangeException re)
	{
		cout << "RangeException: ";
		cout << re.getMsg() << endl;
		cout << "Bad position = " << re.getPos() << endl;
		exit(1);
	}
	catch (SizeException se)
	{
		cout << "SizeException: ";
		cout << se.getMsg() << endl;
		cout << "Bad value = " << se.getVal() << endl;
		exit(2);
	}

	return 0;
}


