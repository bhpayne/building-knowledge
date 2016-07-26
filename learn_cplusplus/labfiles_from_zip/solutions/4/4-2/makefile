4-2: 4-2.o MyDate.o
	g++ -o 4-2 4-2.o MyDate.o

4-2.o: 4-2.cpp MyDate.h
	g++ -c 4-2.cpp

MyDate.o: MyDate.cpp MyDate.h
	g++ -c MyDate.cpp

clean:
	rm 4-2 *.o

