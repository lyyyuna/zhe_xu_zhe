#include <iostream>

using namespace std;

int count(int num)
{
    int cnt = 0;
    while (num)
    {
        cnt ++;
        num = (num-1) & num;
    }

    return cnt;
}

int main()
{
    cout << count(15) << endl;
}