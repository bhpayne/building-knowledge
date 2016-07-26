7-3: 7-3.o Marketing.o Sales.o Legal.o Accounting.o Employee.o Contractor.o Worker.o
	g++ -o 7-3 7-3.o Marketing.o Sales.o Legal.o Accounting.o Employee.o Contractor.o Worker.o

7-3.o: 7-3.cpp Marketing.h Sales.h Legal.h Accounting.h Contractor.h Worker.h
	g++ -c 7-3.cpp

Worker.o: Worker.cpp Worker.h
	g++ -c Worker.cpp

Contractor.o: Contractor.cpp Contractor.h Worker.h
	g++ -c Contractor.cpp

Employee.o: Employee.cpp Employee.h Worker.h
	g++ -c Employee.cpp

Sales.o: Sales.cpp Sales.h Employee.h Worker.h
	g++ -c Sales.cpp

Marketing.o: Marketing.cpp Marketing.h Employee.h Worker.h
	g++ -c Marketing.cpp

Legal.o: Legal.cpp Legal.h Contractor.h Worker.h
	g++ -c Legal.cpp

Accounting.o: Accounting.cpp Accounting.h Contractor.h Worker.h
	g++ -c Accounting.cpp

clean:
	rm 7-3 *.o

