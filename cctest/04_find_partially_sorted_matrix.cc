#include <iostream>
#include <vector>

using namespace std;

bool find_in_matrix(int * matrix, int rows, int columns, int target)
{
    // bool found = false;
    int i = 0;
    int j = columns - 1;

    while (i < rows && j > -1)
    {
        if (matrix[i*columns+j] == target)
            return true;
        if (matrix[i*columns+j] > target)
            j--;
        else
            i++;
    }

    return false;
}

int main()
{
    int matrix[][4] = {{1, 2, 8, 9}, {2, 4, 9, 12}, {4, 7, 10, 13}, {6, 8, 11, 15}};
    cout << find_in_matrix((int *)matrix, 4, 4, 7) << endl;
    cout << find_in_matrix((int *)matrix, 4, 4, 17) << endl;

}