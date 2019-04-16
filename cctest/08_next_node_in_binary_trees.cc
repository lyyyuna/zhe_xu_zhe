#include <iostream>

using namespace std;

class TreeNode
{
public:
    int val;
    TreeNode * pparent;
    TreeNode * pleft;
    TreeNode * pright;

    TreeNode(int val):val(val)
    {
        pparent = nullptr;
        pleft = nullptr;
        pright = nullptr;
    }
};

TreeNode * get_node(TreeNode * pnode)
{
    if (pnode == nullptr)
        return nullptr;

    if (pnode->pright != nullptr)
    {
        TreeNode * ptemp = pnode->pright;
        while (ptemp->pleft)
        {
            ptemp = ptemp->pleft;
        }
        return ptemp;
    } else if (pnode->pparent != nullptr) {
        TreeNode * pcur = pnode;
        TreeNode * pparent = pnode->pparent;
        while (pparent->pleft != pcur)
        {
            pcur = pparent;
            pparent = pcur->pparent;
        }
        return pparent;
    }

    return nullptr;
}

int main()
{

}