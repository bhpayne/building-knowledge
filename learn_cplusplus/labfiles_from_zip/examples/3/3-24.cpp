#include <iostream>

int n1 = 50, n2 = 100;

void fun( )
{
   std::cout << n1 << std::endl;    // prints 50
   std::cout << n2 << std::endl;    // prints 100
}

main( )
{
   int n1 = 500, n2 = 1000;
   
   fun( );
   
   std::cout << n1 << std::endl;    // prints 500
   std::cout << n2 << std::endl;    // prints 1000
   
   std::cout << ::n1 << std::endl;  // prints 50
   std::cout << ::n2 << std::endl;  // prints 100   
}

