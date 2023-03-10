#include <iostream>
using namespace std;

void Patern7()
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
}
int star = 1;

void Pattern8(int i, int star)
{
    if (i != 5)
    {
        star = star + 2;
        i++;
        Pattern8(i, star);
        i--;
        star = star - 2;
    }
    for (int k = i; k != 5; k++)
    {
        cout << " ";
    }
    for (int j = 1; j <= star; j++)
    {
        cout << "*";
    }

    // cout << " i " << i << " star " << star;
    cout << endl;
}

int main()
{
    Patern7();
    Pattern8(1, star);
    return 0;
}