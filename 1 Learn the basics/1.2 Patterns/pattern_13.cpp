#include <iostream>
using namespace std;

int main()
{

    int i, val = 1, j;
    for (i = 1; i <= 5; i++)
    {
        for (j = 1; j <= i; j++)
        {
            cout << " " << val;
            val++;
        }
        cout << endl;
    }
    return 0;
}