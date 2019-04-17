#include <iostream>

using namespace std;

class ListNode
{
public:
    int val;
    ListNode * pnext;

    ListNode(int v, ListNode * n=nullptr):val(v), pnext(n)
    {
    }
};

ListNode * reverselist(ListNode * phead)
{
    ListNode * preversehead = nullptr;
    ListNode * pnode = phead;
    ListNode * pprev = nullptr;

    while (pnode)
    {
        ListNode * next = pnode->pnext;
        if (next == nullptr)
        {
            preversehead = pnode;
        }
        pnode->pnext = pprev;
        pprev = pnode;
        pnode = next;
    }
    return preversehead;
}

int main()
{
    ListNode n5(5);
    ListNode n4(4, &n5);
    ListNode n3(3, &n4);
    ListNode n2(2, &n3);
    ListNode n1(1, &n2);

    ListNode * p = reverselist(&n1);
    while (p)
    {
        cout << p->val << " ";
        p = p->pnext;
    }
    cout << endl;

    return 0;
}