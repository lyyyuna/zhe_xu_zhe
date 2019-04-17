#include <iostream>

using namespace std;

bool isodd(int num)
{
    return num%2 == 1;
}

bool iseven(int num)
{
    return num%2 == 0;
}

void reorder(int * arr, int length)
{
    int * p1 = arr;
    int * p2 = arr + length-1;

    while (p1 < p2)
    {
        while (p1 < p2 && isodd(*p1))
        {
            p1 ++;
        }
        while (p1 < p2 && iseven(*p2))
        {
            p2 --;
        }

        int temp = *p1;
        *p1 = *p2;
        *p2 = temp;
    }
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    reorder(arr, 5);
    for(int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}