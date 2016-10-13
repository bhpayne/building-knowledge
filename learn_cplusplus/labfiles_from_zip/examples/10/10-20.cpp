//
//	10-20.cpp
//
#include <iostream>
#include <deque>
#include <queue>

using namespace std;

int main()
{
	int value, ans;
	priority_queue <int> q;
	
	while(1)
	{
		cout << "0) quit\n1) insert\n2) remove" << endl << "-> ";
		cin >> ans;
		
		if (ans == 0)
			break;
		else if (ans == 1)
	    {
			cout << "insert" << endl;
			cout << "enter value ";
			cin >> value;
			q.push(value);
		}
		else if (ans == 2)
		{
			if ( q.empty())
				cout << "empty" << endl;
			else
			{
				cout << "removing " << q.top() << endl;
				q.pop();
			}
		}
	}
	
	while(! q.empty()) {
		cout << q.top() << " " ;
		q.pop();
	}
	cout << endl;
	
	return 0;
}

