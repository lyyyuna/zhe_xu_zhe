#include <iostream>
#include <vector>
#include <stack>

using namespace std;

bool ispoporder(vector<int> & ppush, vector<int> & ppop)
{
    int p1 = 0;
    int p2 = 0;
    stack<int> s1;
    auto size = ppush.size();
    while (p2 <= size-1)
    {
        while (s1.empty() || s1.top() != ppop[p2])
        {
            if (p1 > size-1) 
                break;
            s1.push(ppush[p1]);
            p1++;
        }
        if (s1.top() != ppop[p2])
            return false;

        p2++;
        s1.pop();
    }

    return true;
}

int main()
{
    vector<int> p1 = {1, 2, 3, 4, 5};
    vector<int> p2 = {4, 5, 3, 2, 1};

    cout << ispoporder(p1, p2) << endl;

}