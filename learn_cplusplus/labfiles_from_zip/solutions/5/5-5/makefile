5-5: 5-5.o MyString.o
	g++ -o 5-5 5-5.o MyString.o

5-5.o: 5-5.cpp MyString.h
	g++ -c 5-5.cpp

MyString.o: MyString.cpp MyString.h
	g++ -c MyString.cpp

clean:
	rm 5-5 *.o

