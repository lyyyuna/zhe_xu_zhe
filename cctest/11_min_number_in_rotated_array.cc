#include <iostream>

using namespace std;

int min(int * numbers, int length)
{
    int index1 = 0;
    int index2 = length-1;
    int indexmid = 0;

    while (numbers[index1]>numbers[index2])
    {
        if (index2-index1 == 1)
        {
            indexmid = index2;
            break;
        }
        indexmid = index1 + (index2-index1)/2;
        if (numbers[indexmid] >= numbers[index1])
            index1 = indexmid;
        if (numbers[indexmid] <= numbers[index2])
            index2 = indexmid;
    }

    return numbers[indexmid];
}

int main()
{
    int arr[] = {3, 4, 5, 1, 2};
    cout << min(arr, 5) << endl;
}