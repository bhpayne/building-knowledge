5-3: 5-3.o IntArray.o
	g++ -o 5-3 5-3.o IntArray.o

5-3.o: 5-3.cpp IntArray.h
	g++ -c 5-3.cpp

IntArray.o: IntArray.cpp IntArray.h
	g++ -c IntArray.cpp

clean:
	rm 5-3 *.o

