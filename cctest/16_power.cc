#include <iostream>
#include <cmath>

using namespace std;

bool equal(double a, double b)
{
    if (a-b < 0.0001 && b-a < 0.0001)
        return true;
    return false;
}

double _power(double base, int exponent)
{
    if (equal(base, 0) && exponent == 0)
        return 0.0;
    
    int absexpo = abs(exponent);
    double res = 1.0;
    for (int i = 0; i < absexpo; i++)
        res *= base;
    if (exponent < 0)
        res = 1.0/res;
    return res;
}

int main()
{
    cout << _power(4, 4) << endl;
    cout << _power(2, -1) << endl;
}