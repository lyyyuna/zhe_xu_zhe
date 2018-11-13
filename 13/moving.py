def movingCount(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    for r in matrix:
        if len(r) != cols:
            return False

    visited = [[False] * cols for _ in range(rows)]
    count = countRecursively(matrix, k, (0, 0), visited)
    return count


def countRecursively(matrix, k, matrixIndices, visited):
    count = 0
    x, y = matrixIndices
    if check(matrix, k, matrixIndices, visited):
        count = 1 + countRecursively(matrix, k, (x+1, y), visited) +
                    countRecursively(matrix, k, (x-1, y), visited) +
                    countRecursively(matrix, k, (x, y+1), visited) +
                    countRecursively(matrix, k, (x, y-1), visited)

    return count


def check(matrix, k, matrixIndices, visited):
    m_i, m_j = matrix_indices
    if not (0 <= m_i < len(matrix)) or not (0 <= m_j < len(matrix[0])) or \
            (sum_digit(m_i) + sum_digit(m_j) > k) or \
            visited[m_i][m_j]:
        return False
    return True


def sum_digit(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum