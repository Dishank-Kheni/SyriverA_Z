#include <iostream>
using namespace std;

void Pattern2()
{
    int i = 0, j = 0;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j <= i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

void Pattern5()
{
    int i = 0, j = 0;
    for (i = 1; i <= 5 - 1; i++)
    {
        for (j = i; j <= 5 - 1; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

int main()
{
    Pattern2();
    // cout << endl;
    Pattern5();
    return 0;
}