#include <iostream>
#include <vector>
#include <string>

using namespace std;

string replace_spaces(vector<char> str)
{
    size_t len = str.size();
    size_t p1 = len-1;
    int count = 0;
    for (auto it = str.begin(); it != str.end(); it ++)
    {
        if (*it == ' ')
        {
            count += 2;
        }
    }
    str.resize(len+count);
    size_t p2 = len+count-1;
    while (p1 != p2)
    {
        if (str[p1] != ' ')
        {
            str[p2] = str[p1];
            p2 --;
        } else {
            str[p2-2] = '%';
            str[p2-1] = '2';
            str[p2] = '0';
            p2 -= 3;
        }
        p1 --;
    }

    return string(str.begin(), str.end());
}

int main()
{
    string test_str = "hello world";
    cout << replace_spaces(vector<char>(test_str.begin(), test_str.end())) << endl;
}