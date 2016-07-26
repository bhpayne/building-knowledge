//
// Starter for Exercise 7-3
//

#include "Marketing.h"
#include "Sales.h"
#include "Legal.h"
#include "Accounting.h"
#include "Worker.h"
#include "Employee.h"
#include "Contractor.h"

int main()
{
    const int SIZE = 4;
    
	Marketing bob("Chief Marketer");
	Sales kim("Head of Sales");
	Legal steven("Law Dept");
	Accounting paul("CPA");

	Worker *pt[SIZE] = { &bob, &kim, &steven, &paul };
	
    int i;
	for (i = 0; i < SIZE; i++)
	{
		cout << pt[i] -> getId() << " " ;
		cout << pt[i] -> getName() << " ";
		pt[i] -> pay();
		pt[i] -> vacation();
		cout << "=====" << endl;
	}

	Employee *pte[SIZE/2] = { &kim, &bob };

	for (i = 0; i < SIZE/2; i++)
	{
		cout << pte[i] -> pension() << " " ;
		pte[i] -> bonus();
		cout << "=====" << endl;
	}

	Contractor *ptc[SIZE/2] = { &steven, &paul };

	for (i = 0; i < SIZE/2; i++)
	{
		ptc[i] -> review();
		cout << "=====" << endl;
	}
	
	return 0;
}

