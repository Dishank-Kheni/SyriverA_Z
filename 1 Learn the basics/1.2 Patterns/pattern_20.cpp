#include <iostream>
using namespace std;

void PatternUp()
{
    int i, j;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5 - i; j++)
        {
            if (i == 0)
                break;
            cout << "*";
        }
        for (j = (5 * 2); j > (5 * 2) - (2 * i); j--)
        {
            if (i == 0)
                break;
            cout << " ";
        }
        for (j = 0; j < 5 - i; j++)
        {
            if (i == 0)
                break;
            cout << "*";
        }
        if (i != 0)
            cout << endl;
    }
}

void PatternDown()
{
    int i, l, m, n;
    for (i = 1; i <= 5; i++)
    {

        for (l = 1; l <= i; l++)
        {

            cout << "*";
        }
        for (m = 1; m <= (5 * 2) - (i * 2); m++)
        {

            cout << " ";
        }
        for (n = i; n >= 1; n--)
        {

            cout << "*";
        }
        cout << endl;
    }
}

int main()
{
    PatternDown();
    PatternUp();
    return 0;
}