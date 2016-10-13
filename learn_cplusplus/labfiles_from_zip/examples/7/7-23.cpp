//
//	7-23.cpp
//
#include <iostream>
#include <string>

using namespace std;

class Animal
{
private:    
	static int ids;
	
protected:
	int id;
	string name;
	
public:
	Animal(string);
	int getID() const;
	virtual void speak() const;
};

int Animal::ids = 1;

Animal::Animal(string n)
{
	name = n;
	id = ids++;
}

int Animal::getID() const
{
		return id;
}

void Animal::speak() const
{
		cout << "What a zoo" << endl;
}

//===========================================

class Dog : public Animal
{
public:
	Dog(string);
	virtual void speak() const;
};

Dog::Dog(string n) : Animal(n) {}

void Dog::speak() const
{
    cout << "My name is " << name << ": " << "Woof" << endl;
}

//==============================================

class Lion : public Animal
{
public:
	Lion(string);
	virtual void speak() const;
};

Lion::Lion(string n) : Animal(n) {}

void Lion::speak() const
{
	cout << "My name is " << name << ": " << "Roooaaaarrrr" << endl;
}

//==============================================

class Collection
{
private:    
	int capacity;
	int howmany;
	Animal **p;
	
public:
	Collection(int number = 10);

	void addAnimal(Animal & pt);
	
	Animal * operator[](int pos);
	
	int size();
};

Collection::Collection(int number)
{
	capacity = number;
	p = new Animal *[capacity];
	howmany = 0;
}

void Collection::addAnimal(Animal & pt)
{
	if ( howmany < capacity )
		p[howmany++] = &pt;
	else
		cout << "rejected " << pt.getID() << "\n";
}

Animal * Collection::operator[](int pos)
{
	if ( pos >= 0 && pos < howmany )
		return p[pos];
	else {
		cout << "Bad value: " << pos << "\n";
		return 0;
	}
}

int Collection::size()
{
	return howmany;
}

//==============================================

int main()
{
	Collection zoo(10);

	Animal ani("mal");
	Dog zip("zippy");
	Dog chip("chippy");
	Lion leo("leo");

	zoo.addAnimal(zip);
	zoo.addAnimal(chip);
	zoo.addAnimal(leo);
	zoo.addAnimal(ani);

	for (int i = 0; i < zoo.size(); i++)
		zoo[i] -> speak();
		
	return 0; 
}
			
