#include <iostream>
using namespace std;

int totalSUM = 0;

void fun(int n)
{
    int SUM = 0;
    int remainingElement = 0;
    if (n <= 4)
    {
        SUM = n + (n - 1);
        totalSUM = SUM;
        fun(++n);
        --n;
        remainingElement = totalSUM - SUM;
        int temp = 4;
        if (remainingElement != 0)
        {
            for (int i = 1; i <= (remainingElement / 2); i++)
            {
                cout << temp;
                temp--;
            }
        }
        for (int i = 1; i <= SUM; i++)
        {
            cout << n;
        }
        if (remainingElement != 0)
        {
            for (int i = 5 - (remainingElement / 2); i <= 4; i++)
            {
                cout << i;
            }
        }
        // cout << " n " << n;
        // cout << " Remaining Element " << remainingElement;
        // cout << " sum " << SUM;
        cout << endl;
    }
}

void fun2(int n)
{

    // n--;
    int SUM = n + (n - 1);
    int remainingElement = totalSUM - SUM;
    int temp = 4;

    if (remainingElement != 0)
    {
        for (int i = 1; i <= (remainingElement / 2); i++)
        {
            cout << temp;
            temp--;
        }
    }
    for (int i = 1; i <= SUM; i++)
    {
        cout << n;
    }
    if (remainingElement != 0)
    {
        for (int i = 5 - (remainingElement / 2); i <= 4; i++)
        {
            cout << i;
        }
    }
    cout << endl;
    if (n < 4)
    {
        fun2(++n);
    }
}

int main()
{
    fun(1);
    fun2(2);
    return 0;
}