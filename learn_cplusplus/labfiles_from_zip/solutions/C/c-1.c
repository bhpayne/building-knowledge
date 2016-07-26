//
//	Exercise 3-1
//
//      Write an account structure which takes a name, an account
//      number and an initial balance.
//
#include <stdio.h>
#include <string.h>
struct Account {
    char name[20];
    int account;
    double balance;
};
struct Account fill(char *name, int number, double balance)
{
    struct Account temp;
    strcpy(temp.name,name);
    temp.account = number;
    temp.balance = balance;
    return temp;
}
void print(struct Account param)
{
    printf("%s: %d: %.2f\n", param.name, param.account, param.balance);
}
struct Account deposit(struct Account param, double balance)
{
	param.balance += balance;
	return param;
}
main()
{
    struct Account person;
	person = fill("mike", 100, 1000.00);
    print(person);
	person = deposit(person,50.00);
	print(person);
}
