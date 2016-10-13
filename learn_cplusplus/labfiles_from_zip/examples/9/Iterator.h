//
//  Iterator.h
//

#ifndef ITERATOR_H
#define ITERATOR_H

#include "List.h"

class Iterator 
{
private:    
    List::Item *currentItem;
    
public:
    Iterator(const List & aList);
    Iterator operator++();
    int operator*();
    bool atEnd() { return (currentItem == 0); }
};

#endif

