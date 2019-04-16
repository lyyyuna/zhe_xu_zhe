#include <iostream>

using namespace std;

int getdigitsum(int number)
{
    int sum = 0;
    while (number > 0)
    {
        sum += number % 10;
        number /= 10;
    }

    return sum;
}

bool check (int threshold, int rows, int cols, int row, int col, int * visited)
{
    if (row >= 0 && col < cols && col >= 0 && col < cols
            && getdigitsum(row)+getdigitsum(col) <= threshold
            && visited[row*cols + col] == false)
        return true;
    
    return false;
}

int dfs(int threshold, int rows, int cols, int row, int col, int * visited)
{
    int count = 0;
    if (check(threshold, rows, cols, row, col, visited))
    {
        visited[row * cols + col] = true;
        count += 1 + dfs(threshold, rows, cols, row-1, col, visited)
                   + dfs(threshold, rows, cols, row, col-1, visited)
                   + dfs(threshold, rows, cols, row+1, col, visited)
                   + dfs(threshold, rows, cols, row, col+1, visited);
    }

    return count;
}

int moving_count(int threshold, int rows, int cols)
{
    bool * visited = new bool[rows * cols];

    for (int i = 0; i < rows * cols; i++)
    {
        visited[i] = false;
    }


    
}

int main()
{

}