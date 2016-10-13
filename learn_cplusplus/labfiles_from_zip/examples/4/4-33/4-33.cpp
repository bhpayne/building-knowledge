//
//	4-33.cpp
//
#include <iostream>

using namespace std;

#include "Loan.h"

double sumLoans(Loan *loans, int howmany);
double avgInterest(Loan *loans, int howmany);

int main()
{
    Loan loans[] = { Loan("mike", 30, 100000,8.0),
                     Loan("susan", 20, 75000),
                     Loan("erin", 10)
                   };
                   
    double total, avg;
 
    total = sumLoans(loans, 3);
    cout << "loan total: "<< total<< endl;
 
    avg = avgInterest(loans, 3);
    cout << "avg rate: " << avg << endl;
    
    return 0;
 }
 
 double sumLoans(Loan *loans, int howmany)
 {
    double total = 0.0;
    
    for (int i = 0; i < howmany; i++)
       total += loans[i].getAmount();
       
    return total;
 }
 
 double avgInterest(Loan *loans, int n)
 {
    double avg = 0.0;
    
    for (Loan *p = loans; p < loans + n; p++)
       avg += p -> getRate();
       
    return avg/n;
 }
