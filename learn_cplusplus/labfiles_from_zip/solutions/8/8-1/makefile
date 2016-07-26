8-1: 8-1.o MyString.o
	g++ -o 8-1 8-1.o MyString.o

8-1.o: 8-1.cpp MyString.h
	g++ -c 8-1.cpp

MyString.o: MyString.cpp MyString.h
	g++ -c MyString.cpp

clean:
	rm 8-1 *.o

