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

ListNode * merge_list(ListNode * p1, ListNode * p2)
{
    if (p1 == nullptr)
        return p2;
    if (p2 == nullptr)
        return p1;

    ListNode *p;
    if (p1->val <= p2->val)
    {
        p = p1;
        p->pnext = merge_list(p1->pnext, p2);
    } else {
        p = p2;
        p->pnext = merge_list(p1, p2->pnext);
    }

    return p;
}

int main()
{
    ListNode n5(5);
    ListNode n4(4, &n5);
    ListNode n3(3, &n4);
    ListNode n2(9);
    ListNode n1(1, &n2);

    ListNode * p = merge_list(&n1, &n3);

    while (p)
    {
        cout << p->val << " ";
        p = p->pnext;
    }
    cout << endl;

    return 0;    
}