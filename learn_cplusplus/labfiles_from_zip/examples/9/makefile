all: 9-7 9-14 9-18 9-19 9-22 9-29 9-10

9-7: 9-7.cpp Stack.h Stack.cpp
	g++ -o 9-7 9-7.cpp

9-10: 9-10.cpp
	g++ -o 9-10 9-10.cpp

9-14: 9-14.cpp
	g++ -o 9-14 9-14.cpp


9-18: 9-18.o List.o
	g++ -o 9-18 9-18.o List.o

9-18.o: 9-18.cpp List.h
	g++ -c 9-18.cpp


9-19: 9-19.o List.o
	g++ -o 9-19 9-19.o List.o

9-19.o: 9-19.cpp List.h
	g++ -c 9-19.cpp

List.o: List.cpp List.h
	g++ -c List.cpp


9-22: 9-22.o List.o Iterator.o
	g++ -o 9-22 9-22.o List.o Iterator.o

9-22.o: 9-22.cpp List.h Iterator.h
	g++ -c 9-22.cpp

Iterator.o: Iterator.cpp Iterator.h List.h
	g++ -c Iterator.cpp


9-29:	9-29.o Vector.o SizeException.o RangeException.o
	g++ -o 9-29 9-29.o Vector.o SizeException.o RangeException.o

9-29.o: 9-29.cpp Vector.h SizeException.h RangeException.h
	g++ -c 9-29.cpp

Vector.o: Vector.cpp Vector.h SizeException.h RangeException.h
	g++ -c Vector.cpp

SizeException.o: SizeException.cpp SizeException.h
	g++ -c SizeException.cpp

RangeException.o: RangeException.cpp RangeException.h
	g++ -c RangeException.cpp


clean:
	rm 9-7 9-14 9-18 9-19 9-22 9-29 *.o


