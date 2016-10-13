5-1: 5-1.o Fraction.o
	g++ -o 5-1 5-1.o Fraction.o

5-1.o: 5-1.cpp Fraction.h
	g++ -c 5-1.cpp

Fraction.o: Fraction.cpp Fraction.h
	g++ -c Fraction.cpp

clean:
	rm 5-1 *.o

