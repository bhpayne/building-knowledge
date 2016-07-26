5-2: 5-2.o IntArray.o
	g++ -o 5-2 5-2.o IntArray.o

5-2.o: 5-2.cpp IntArray.h
	g++ -c 5-2.cpp

IntArray.o: IntArray.cpp IntArray.h
	g++ -c IntArray.cpp

clean:
	rm 5-2 *.o

