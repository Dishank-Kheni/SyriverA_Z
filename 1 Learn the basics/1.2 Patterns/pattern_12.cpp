#include <iostream>
using namespace std;

int main()
{
    int i, l, m, n;
    for (i = 1; i <= 4; i++)
    {
        for (l = 1; l <= i; l++)
        {
            cout << l;
        }
        for (m = 1; m <= (4 * 2) - (i * 2); m++)
        {
            cout << " ";
        }
        for (n = i; n >= 1; n--)
        {
            cout << n;
        }
        cout << endl;
    }
    return 0;
}