#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class BinaryTreeNode
{
public:
    int val;
    BinaryTreeNode * pleft;
    BinaryTreeNode * pright;

    BinaryTreeNode(int value):val(value)
    {
        pleft = nullptr;
        pright = nullptr;
    }
};

BinaryTreeNode * construct(int * preorder, int * preorderend, int * inorder, int * inorderend)
{
    int root_val = preorder[0];
    BinaryTreeNode * root = new BinaryTreeNode(root_val);
    if (preorder == preorderend) 
        return root;

    int * rootinorder = inorder;
    while (rootinorder < inorderend && root_val != *rootinorder)
        rootinorder++;
    int len = rootinorder - inorder;
    if (len > 0)
    {
        root->pleft = construct(preorder+1, preorder+len, inorder, rootinorder-1);
    }
    if (len < preorderend - preorder)
    {
        root->pright = construct(preorder+len+1, preorderend, rootinorder+1, inorderend);
    }
    return root;
}

int main()
{
    int preorder[] = {1, 2, 4, 7, 3, 5, 6, 8};
    int inorder[] = {4, 7, 2, 1, 5, 3, 8, 6};

    auto p = construct(preorder, preorder+7, inorder, inorder+7);

    return 0;
}