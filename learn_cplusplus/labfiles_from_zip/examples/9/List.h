//
//  List.h
//

#ifndef LIST_H
#define LIST_H

class List 
{
private:    
    int howmany;            // # of elements in the list
    
    mutable int reps;       // total # of links that have been followed
                            //  (for informational purposes only)

                            // "mutable" allows this data item to
                            //  be modifed by a const member function
	struct Item {
        int data;
		Item *next;
		
	    Item (int value) : data(value), next(0) { }
	};
	
	Item *head;
	Item *tail;
	
public:
	List( );
	~List( );

	unsigned int length( ) const   { return howmany; }
	int getReps() const            { return reps; }
	
	void insert(int newElement);
	
	int operator[ ](int position) const;

	friend class Iterator;
};

#endif

