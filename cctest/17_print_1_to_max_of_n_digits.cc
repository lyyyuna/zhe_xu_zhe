#include <iostream>
#include <vector>

using namespace std;

void print(vector<char> & number)
{
    bool zeroflag = true;
    for (auto it = number.begin(); it != number.end(); it++)
    {    
        if (*it != '0' && zeroflag == true)
            zeroflag = false;
        if (zeroflag == false)
            cout << *it;
    }
    cout << endl;
}

void printdigits(vector<char> & number, int length, int index)
{
    if (index == length)
    {
        print(number);
        return;
    }
    for (int i = 0; i < 10; i++)
    {
        number[index] = i + '0';
        printdigits(number, length, index+1);
    }    
}

void printdigits(int n)
{
    vector<char> number(n, '0');

    printdigits(number, n, 0);

}

int main()
{
    printdigits(2);
}