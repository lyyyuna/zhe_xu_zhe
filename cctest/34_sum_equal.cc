#include <iostream>
#include <vector>

using namespace std;

class TreeNode
{
public:
    int val;
    TreeNode * pleft;
    TreeNode * pright;
    TreeNode(int v):val(v){}
};

void find_path(TreeNode * proot, vector<TreeNode *> & path, 
        int expectedsum, int currentsum)
{
    path.push_back(proot);
    currentsum += proot->val;
    if (proot->pleft == nullptr && proot->pright == nullptr)
    {
        if (currentsum == expectedsum)
        for (auto it = path.begin(); it != path.end(); it++)
        {
            cout << (*it)->val << " ";
        }
        cout << endl;
    }

    if (proot->pleft)
    {
        find_path(proot->pleft, path, expectedsum, currentsum);
    }

    if (proot->pright)
    {
        find_path(proot->pright, path, expectedsum, currentsum);
    }

    path.pop_back();
}

int main()
{
    
}