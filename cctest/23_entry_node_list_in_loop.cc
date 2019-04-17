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

ListNode * findloop(ListNode * phead)
{
    if (phead == nullptr)
        return nullptr;

    ListNode * pslow = phead;
    ListNode * pquick = phead;

    while (true)
    {
        for (int i = 0; i < 2; i++)
        {
            pquick = pquick->pnext;
            if (pquick == nullptr)
                return nullptr;
        }
        pslow = pslow->pnext;

        if (pslow == pquick)
            break;
    }

    int cnt = 1;
    while (true)
    {
        pslow = pslow->pnext;
        if (pslow == pquick)
            break;
        cnt ++;
    }

    pslow = phead;
    pquick = phead;

    for (int i = 0; i < cnt; i++)
    {
        pslow = pslow->pnext;
    }

    while (pslow != pquick)
    {
        pslow = pslow->pnext;
        pquick = pquick->pnext;
    }

    return pslow;
}

int main()
{

}