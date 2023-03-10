#include <iostream>
using namespace std;

int main()
{
    int i = 1, j = 1;
    for (i = 0; i < 5; i++)
    {
        for (j = 1; j <= 5 - i; j++)
        {
            cout << " " << j;
        }
        cout << endl;
    }
    return 0;
}