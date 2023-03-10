#include <iostream>
using namespace std;

int main()
{

    int i, j;
    for (i = 1; i <= 5; i++)
    {
        if (i == 1 || i == 5)
        {
            for (j = 1; j <= 5 - 1; j++)
            {
                cout << "*";
            }
        }
        else
        {
            cout << "*";

            for (j = 1; j <= 5 - 3; j++)
            {
                cout << " ";
            }
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}