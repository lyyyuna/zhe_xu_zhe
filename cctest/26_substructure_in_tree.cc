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

bool hassamestructure(TreeNode * p1, TreeNode * p2)
{
    if (p2 == nullptr)
        return true;
    if (p1 == nullptr)
        return false;

    if (p1->val != p2->val)
        return false;

    return hassamestructure(p1->pleft, p2->pleft) &&
            hassamestructure(p1->pright, p2->pright);
}

bool hassameroot(TreeNode * p1, TreeNode * p2)
{
    bool result = false;
    if (p1 && p2)
    {
        if (p1->val == p2->val)
            result = hassamestructure(p1, p2);
        if (!result)
            result = hassameroot(p1->pleft, p2);
        if (!result)
            result = hassameroot(p1->pright, p2);
    }

    return result;
}

int main()
{

}