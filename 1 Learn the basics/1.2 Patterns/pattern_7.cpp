#include <iostream>
using namespace std;

int main()
{
    int star = 1;
    int i = 0, j = 0;
    for (i = 1; i <= 5; i++)
    {

        for (j = 1; j <= 5 - i; j++)
        {
            cout << " ";
        }
        for (j = 1; j <= star; j++)
        {
            cout << "*";
        }
        star = star + 2;

        cout << endl;
    }
    return 0;
}