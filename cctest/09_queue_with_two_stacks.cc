#include <iostream>
#include <stack>

using namespace std;

class CQueue
{
private:
    stack<int> stack1;
    stack<int> stack2;

public:
    void append(int val)
    {
        stack1.push(val);
    }
    int popleft()
    {
        if (stack2.empty())
        {
            while (!stack1.empty())
            {
                int val = stack1.top();
                stack1.pop();
                stack2.push(val);
            }
        }
        int val = stack2.top();
        stack2.pop();
        return val;
    }
};

int main()
{
    CQueue cq;
    cq.append(1);
    cq.append(2);
    cq.append(3);
    cout << cq.popleft() << endl;
    cout << cq.popleft() << endl;
    cout << cq.popleft() << endl;
    return 0;
}