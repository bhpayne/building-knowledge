//
//	4-7.cpp
//
#include <iostream>
#include <string>
using namespace std;

struct Loan
{   
    string name;
    double amount, rate;
    int years;

    string getName()
    { 
      return name; 
    }
    
    double getAmount()
    { 
       return amount; 
    }
    
    int getYears()
    { 
       return years; 
    }
    
    double getRate()
    { 
       return rate; 
    }
    
    void setName(string n)
    { 
       name = n;
    }
    
    void setAmount(double a)
    { 
       amount = a; 
    }
    
    void setYears(int y) { 
       years = y;
    }
    
    void setRate(double r) { 
       rate = r; 
    }
};

int main()
{
    Loan myLoan;
    
    myLoan.setName("michael");
    myLoan.setYears(30);
    myLoan.setAmount(100000);
    myLoan.setRate(8);
    
    cout << myLoan.getName() << " ";
    cout << myLoan.getAmount() << " ";
    cout << myLoan.getRate() << " ";
    cout << myLoan.getYears() << endl;

    return 0;
}
