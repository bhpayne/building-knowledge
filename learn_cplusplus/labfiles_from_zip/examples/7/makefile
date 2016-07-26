all: 7-14 7-21 7-23 7-8


7-8: 7-8.o Loan.o Mortgage.o 
	g++ -o 7-8 7-8.o Loan.o Mortgage.o 

7-8.o: 7-8.cpp Loan.h Mortgage.h 
	g++ -c 7-8.cpp

Mortgage.o: Mortgage.cpp Mortgage.h Loan.h
	g++ -c Mortgage.cpp

Loan.o: Loan.cpp Loan.h
	g++ -c Loan.cpp


7-14: 7-14.cpp 
	g++ -o 7-14 7-14.cpp

7-21: 7-21.cpp 
	g++ -o 7-21 7-21.cpp

7-23: 7-23.cpp 
	g++ -o 7-23 7-23.cpp


clean:
	rm 7-14 7-21 7-23 *.o

