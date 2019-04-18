#include <iostream>
#include <queue>

using namespace std;

class TreeNode
{
public:
    int val;
    TreeNode * pleft;
    TreeNode * pright;
    TreeNode(int v):val(v){}
};

void printtree(TreeNode * proot)
{
    queue<TreeNode *> q;
    q.push(proot);
    while (!q.empty())
    {
        TreeNode * n = q.front();
        q.pop();
        cout << n->val << " ";
        if (n->pleft)
            q.push(n->pleft);
        if (n->pright)
            q.push(n->pright);
    }
}

int main()
{

}