#include <iostream>

using namespace std;

class Node
{
public:
    int val;
    Node * pnext;
    Node(int v):val(v){}
};

void delete_node(Node * phead, Node * pdel)
{
    if (pdel->pnext != nullptr)
    {
        Node * next = pdel->pnext;
        pdel->val = next->val;
        pdel->pnext = next->pnext;

        delete next;
        next = nullptr;
    }
    if (phead == pdel)
    {
        delete phead;
        phead = nullptr;
    } else {
        Node * pnode = phead;
        while (pnode->pnext != pdel)
            pnode = pnode->pnext;
        pnode->pnext = nullptr;
        delete pdel;
        pdel = nullptr;
    }

}

int main()
{
    
}