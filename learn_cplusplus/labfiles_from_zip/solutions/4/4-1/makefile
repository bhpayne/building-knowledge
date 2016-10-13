4-1: 4-1.o MyDate.o
	g++ -o 4-1 4-1.o MyDate.o

4-1.o: 4-1.cpp MyDate.h
	g++ -c 4-1.cpp

MyDate.o: MyDate.cpp MyDate.h
	g++ -c MyDate.cpp

clean:
	rm 4-1 *.o

