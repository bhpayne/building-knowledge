4-3: 4-3.o MyString.o
	g++ -o 4-3 4-3.o MyString.o

4-3.o: 4-3.cpp MyString.h
	g++ -c 4-3.cpp

MyString.o: MyString.cpp MyString.h
	g++ -c MyString.cpp

clean:
	rm 4-3 *.o

