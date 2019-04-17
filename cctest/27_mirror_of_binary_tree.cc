#include <iostream>

using namespace std;

class TreeNode
{
public:
    int val;
    TreeNode * pleft;
    TreeNode * pright;
    TreeNode(int v):val(v){}
};

void mirror(TreeNode * pnode)
{
    if (pnode == nullptr)
        return;

    if (pnode->pleft == nullptr && pnode->pright == nullptr)
        return;
    
    TreeNode * ptemp = pnode->pleft;
    pnode->pleft = pnode->pright;
    pnode->pright = ptemp;

    if (pnode->pleft)
        mirror(pnode->pleft);
    if (pnode->pright)
        mirror(pnode->pright);
}

int main()
{

}