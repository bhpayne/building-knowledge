7-2: 7-2.o MyString.o Shape.o Circle.o Square.o
	g++ -o 7-2 7-2.o MyString.o Shape.o Circle.o Square.o

7-2.o: 7-2.cpp Shape.h Circle.h Square.h
	g++ -c 7-2.cpp

MyString.o: MyString.cpp MyString.h
	g++ -c MyString.cpp

Shape.o: Shape.cpp Shape.h MyString.h
	g++ -c Shape.cpp

Circle.o: Circle.cpp Circle.h Shape.h MyString.h
	g++ -c Circle.cpp

Square.o: Square.cpp Shape.h Square.h MyString.h 
	g++ -c Square.cpp

clean:
	rm 7-2 *.o

