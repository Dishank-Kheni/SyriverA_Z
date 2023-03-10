#include <iostream>
using namespace std;

int main()
{
    int i = 0, j = 0;
    for (i = 1; i <= 5; i++)
    {
        for (j = i; j <= 5; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}