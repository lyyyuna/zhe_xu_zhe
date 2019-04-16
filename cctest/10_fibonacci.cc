#include <iostream>

using namespace std;

int fibonacci(int n)
{
    if (n == 1)
        return 0;
    if (n == 2)
        return 1;
    int f0 = 0;
    int f1 = 1;
    int fn = 0;
    for (int i = 0; i < n-2; i++)
    {
        fn = f0 + f1;
        f0 = f1;
        f1 = fn;
        
    }

    return fn;
}

int main()
{
    cout << fibonacci(4) << endl;
    cout << fibonacci(6) << endl;
}