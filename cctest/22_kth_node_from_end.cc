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

ListNode * find_k_node(ListNode * phead, int k)
{
    if (phead == nullptr)
        return nullptr;
    ListNode * p1 = phead;

    for (int i = 0; i < k; i++)
    {
        if (p1->pnext == nullptr)
            return nullptr;
        p1 = p1->pnext;
    }

    ListNode * p2 = phead;
    while (p1->pnext)
    {
        p1 = p1->pnext;
        p2 = p2->pnext;
    }

    return p2;
}

int main()
{
    ListNode n5(5);
    ListNode n4(4, &n5);
    ListNode n3(3, &n4);
    ListNode n2(2, &n3);
    ListNode n1(1, &n2);

    ListNode * p = find_k_node(&n1, 1);
    cout << p->val << endl;
}