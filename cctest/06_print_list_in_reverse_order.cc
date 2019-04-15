#include <iostream>
using namespace std;

class ListNode
{
public:
    int         value;
    ListNode*   pnext;

    ListNode(int val):value(val)
    {}

    void connect_node(ListNode * pnode)
    {
        this->pnext = pnode;
    }
};

void print_in_reverse(ListNode * phead)
{
    if (phead == nullptr)
        return;
    print_in_reverse(phead->pnext);
    cout << phead->value << " ";
}

int main() 
{
    auto p1 = ListNode(2);
    auto p2 = ListNode(3);
    auto p3 = ListNode(1);
    p1.connect_node(&p2);
    p2.connect_node(&p3);

    print_in_reverse(&p1);
}