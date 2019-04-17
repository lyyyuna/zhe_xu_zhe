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

bool issym(TreeNode * proot)
{
    return issym(proot, proot);
}

bool issym(TreeNode * p1, TreeNode * p2)
{
    if (p1 == nullptr && p2 == nullptr)
        return true;

    if (p1 == nullptr || p2 == nullptr)
        return false;

    if (p1->val != p2->val)
        return false;

    return issym(p1->pleft, p2->pright) &&
            issym(p1->pright, p2->pleft);
}

int main()
{

}