#include <iostream>
#include <map>
using namespace std;

bool duplicate(int numbers[], int length)
{
    if (numbers == nullptr || length < 0)
        return false;
    
    map<int, int> count_map;
    for (int i  = 0; i < length; i++)
    {
        auto it = count_map.find(numbers[i]);
        if (it != count_map.end())
            count_map[numbers[i]] ++;
        else
            count_map[numbers[i]] = 1;
    }

    for (auto it = count_map.begin(); it != count_map.end(); it++)
    {
        if (it->second > 1)
        {
            cout << it->first << endl;
            return true;
        }
    }

    return false;
}

int main() {
    int num[] = {1, 2, 3, 2, 5};
    duplicate(num, 5);
}