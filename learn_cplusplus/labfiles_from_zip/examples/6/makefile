6-7: 6-7.o Point.o Line.o 
	g++ -o 6-7 6-7.o Point.o Line.o 

6-7.o: 6-7.cpp Point.h Line.h 
	g++ -c 6-7.cpp

Line.o: Line.cpp Line.h Point.h
	g++ -c Line.cpp

Point.o: Point.cpp Point.h
	g++ -c Point.cpp

clean:
	rm 6-7 *.o

