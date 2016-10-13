7-1: 7-1.o Point.o Point3D.o
	g++ -o 7-1 7-1.o Point.o Point3D.o

7-1.o: 7-1.cpp Point.h Point3D.h
	g++ -c 7-1.cpp

Point.o: Point.cpp Point.h
	g++ -c Point.cpp

Point3D.o: Point3D.cpp Point.h Point3D.h
	g++ -c Point3D.cpp

clean:
	rm 7-1 *.o

