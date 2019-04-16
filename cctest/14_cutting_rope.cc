#include <iostream>
#include <vector>

using namespace std;

int maxproduct(int length)
{
    if (length < 2)
        return 0;
    if (length == 2)
        return 1;
    if (length == 3)
        return 2;

    vector<int> prod(length+1);
    prod[0] = 0;
    prod[1] = 1;
    prod[2] = 2;
    prod[3] = 3;

    for (int i = 4; i < length+1; i++)
    {
        int max = 0;
        for (int j = 1; j <= i/2; j++)
        {
            int product = prod[i-j] * prod[j];
            if (max < product)
                max = product;
            prod[i] = max;
        }
    }

    return prod[length];
}

int main()
{
    cout << maxproduct(5) << endl;
    cout << maxproduct(3) << endl;

}
