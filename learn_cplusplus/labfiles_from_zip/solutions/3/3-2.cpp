//
//	Solution 3-2
//
#include <iostream>
using namespace std;

void square(int & left, int & right);
void square(double & left, double & right);
main()
{
        cout << "input two integers ";
        int one, two;
        cin >> one >> two;
        square(one, two);
        cout << "squares are " << one << " and " << two << endl;
        cout << "enter two doubles ";
        double d1, d2;
        cin >> d1 >> d2;
        square(d1,d2);
        cout << "squares are " << d1 << " and " << d2 << endl;
}
void square(double & left, double & right)
{
        left *= left;
        right *= right;
}
void square(int & left, int & right)
{
        right *= right;
        left *= left;
}
