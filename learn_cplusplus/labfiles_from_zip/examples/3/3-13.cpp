 //
 //   3-13.cpp
 //
 #include <iostream>
 struct Fraction
 {
	 int n;
	int d;
	void recip( ) {
		int temp;
		temp = n;
		n = d;
		d = temp;
	}
	void print( ){
		std::cout << n << "/"  << d << "\n";
	}
 };
