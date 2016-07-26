6-2: 6-2.o MyString.o MyDate.o Employee.o Company.o
	g++ -o 6-2 6-2.o MyString.o MyDate.o Employee.o Company.o

6-2.o: 6-2.cpp MyString.h MyDate.h Employee.h Company.h
	g++ -c 6-2.cpp

MyDate.o: MyDate.cpp MyDate.h
	g++ -c MyDate.cpp

MyString.o: MyString.cpp MyString.h
	g++ -c MyString.cpp

Employee.o: Employee.cpp Employee.h MyDate.h MyString.h
	g++ -c Employee.cpp

Company.o: Company.cpp MyString.h MyDate.h Employee.h Company.h
	g++ -c Company.cpp

clean:
	rm 6-2 *.o

