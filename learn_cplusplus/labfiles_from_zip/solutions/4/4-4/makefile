4-4: 4-4.o MyString.o
	g++ -o 4-4 4-4.o MyString.o

4-4.o: 4-4.cpp MyString.h
	g++ -c 4-4.cpp

MyString.o: MyString.cpp MyString.h
	g++ -c MyString.cpp

clean:
	rm 4-4 *.o

