#include <iostream>
using namespace std;

int main()
{
    int i, j, binary = 1;
    for (i = 1; i <= 5; i++)
    {
        binary = i;
        (binary % 2 == 0) ? binary = 0 : binary = 1;
        for (j = 1; j <= i; j++)
        {
            cout << " " << binary;
            (binary == 0) ? binary = 1 : binary = 0;
        }
        cout << endl;
    }
    return 0;
}