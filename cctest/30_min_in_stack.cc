#include <iostream>
#include <stack>

using namespace std;

class minstack
{
private:
    stack<int> s1;
    stack<int> s2;

public:
    void push(int num)
    {
        s1.push(num);

        if (s2.empty() || s2.top()>num)
            s2.push(num);
        else
        {
            s2.push(s2.top());
        }
        
    }

    int pop()
    {
        int v = s1.top();
        s1.pop();
        s2.pop();

        return v;
    }

    int min()
    {
        return s2.top();
    }
};

int main()
{
    minstack m;
    m.push(15);
    m.push(12);
    m.push(21);
    m.push(11);
    m.push(25);

    cout << m.min() << endl;
    m.pop();
    cout << m.min() << endl;
    m.pop();
    cout << m.min() << endl;
}