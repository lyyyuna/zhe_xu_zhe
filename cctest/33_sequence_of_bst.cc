#include <iostream>
#include <vector>

using namespace std;

bool verifybst(int * arr, int len)
{
    if (arr == nullptr || len <= 0)
        return false;

    int root = arr[len-1];

    int index = 0;
    for (; index < len-1; index++)
    {
        if (root < arr[index])
            break;
    }

    int j = index;
    for (; j < len-1; j++)
    {
        if (root > arr[j])
            return false;
    }

    bool left = true;
    bool right = true;
    if (index > 0)
        left = verifybst(arr, index);
    if (index < len-1)
        right = verifybst(arr+index, len-index-1);

    return left && right;
}

int main()
{
    int num[] = {5, 7, 6, 9, 11, 10, 8};

    cout << verifybst(num, 7) << endl;
}