/*

prints the numbers 1 to 10, one number per line
prints the numbers 10 to 1 (counting backwards), one number per line
prints the numbers 1 to 100, 10 numbers per line

Challenge:  Ask the user for the upper limit, whether they want forward or backwards, and how many numbers to print per line.

*/

#include inpu

using std::cout;
using std::endl;

int main(){
 
    cout << "prints the numbers 1 to 10, one number per line" << endl;
    for (int indx=1; indx<=10; indx++){
        cout << indx;
    }
    
    cout << "prints the numbers 10 to 1 (counting backwards), one number per line" << endl;
    for (int indx=10; indx>=1; indx--){
        cout << indx;
    }
    
    cout << "prints the numbers 1 to 100, 10 numbers per line" << endl;
    for (int indx=0; indx<100; indx++){
        if (indx%10==0){
            printf("\n");
        }
        cout << indx+1;
    }
    cout << endl;
    
    int limit=0, direction=0, perline=0;
    cout << "Ask the user for the upper limit");
    cin >> limit;
    cout << "Ask whether they want forward (0) or backwards (1)");
    cin >> direction;
    cout << "Ask how many numbers to print per line");
    cin >> perline;
    
    if (direction==0){
        printf("prints the numbers 1 to %d, %d numbers per line\n",limit,perline);

        for (int indx=0; indx<limit; indx++){
            if (indx%perline==0){
                printf("\n");
            }
            printf("%d,",indx+1);
        }
        printf("\n");


    }else{
        printf("prints the numbers %d to 1, %d numbers per line\n",limit,perline);

        for (int indx=limit; indx>0; indx++){
            if (indx%perline==0){
                printf("\n");
            }
            printf("%d,",indx+1);
        }
        printf("\n");
    }

    
}
