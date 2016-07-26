all: 5-8/5-8 5-14/5-14 5-16 5-19/5-19


5-8/5-8: 5-8/5-8.o 5-8/Fraction.o
	g++ -o 5-8/5-8 5-8/5-8.o 5-8/Fraction.o

5-8/5-8.o: 5-8/5-8.cpp 5-8/Fraction.h
	g++ -c -o 5-8/5-8.o 5-8/5-8.cpp

5-8/Fraction.o: 5-8/Fraction.cpp 5-8/Fraction.h
	g++ -c -o 5-8/Fraction.o  5-8/Fraction.cpp


5-14/5-14: 5-14/5-14.o 5-14/Fraction.o
	g++ -o 5-14/5-14 5-14/5-14.o 5-14/Fraction.o

5-14/5-14.o: 5-14/5-14.cpp 5-14/Fraction.h
	g++ -c -o 5-14/5-14.o 5-14/5-14.cpp

5-14/Fraction.o: 5-14/Fraction.cpp 5-14/Fraction.h
	g++ -c -o 5-14/Fraction.o  5-14/Fraction.cpp


5-16: 5-16.cpp
	g++ -o 5-16 5-16.cpp


5-19/5-19: 5-19/5-19.o 5-19/IntArray.o
	g++ -o 5-19/5-19 5-19/5-19.o 5-19/IntArray.o

5-19/5-19.o: 5-19/5-19.cpp 5-19/IntArray.h
	g++ -c -o 5-19/5-19.o 5-19/5-19.cpp

5-19/IntArray.o: 5-19/IntArray.cpp 5-19/IntArray.h
	g++ -c -o 5-19/IntArray.o  5-19/IntArray.cpp

clean: 
	rm 5-8/5-8 5-8/*.o  5-14/5-14 5-14/*.o 5-16 5-19/5-19 5-19/*.o
