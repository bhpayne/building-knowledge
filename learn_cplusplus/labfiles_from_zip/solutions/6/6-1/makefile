6-1: 6-1.o MyString.o MyDate.o Employee.o
	g++ -o 6-1 6-1.o MyString.o MyDate.o Employee.o

6-1.o: 6-1.cpp MyString.h MyDate.h Employee.h
	g++ -c 6-1.cpp

MyDate.o: MyDate.cpp MyDate.h
	g++ -c MyDate.cpp

MyString.o: MyString.cpp MyString.h
	g++ -c MyString.cpp

Employee.o: Employee.cpp Employee.h MyDate.h MyString.h
	g++ -c Employee.cpp

clean:
	rm 6-1 *.o

