5-4: 5-4.o IntArray.o
	g++ -o 5-4 5-4.o IntArray.o

5-4.o: 5-4.cpp IntArray.h
	g++ -c 5-4.cpp

IntArray.o: IntArray.cpp IntArray.h
	g++ -c IntArray.cpp

clean:
	rm 5-4 *.o

