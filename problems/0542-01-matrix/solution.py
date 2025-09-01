class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distances = [[0] * n for _ in range(m)]  # initialized the distance matrix
        
        # multi-source BFS
        queue = deque()  # use queue for BFS
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    value = 0
                    queue.append((r,c))  # initialize the queue with all cells with the value "0" (i.e., multi-source BFS)
                else:
                    value = float('inf')  # if cell value is 1 (i.e., not 0), initialize the value to "infinity" to mark that it is unvisited
                distances[r][c] = value

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # all four possible directions (excluding diagonals)
        while queue:
            r, c = queue.popleft()
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if (0 <= nr < m) and (0 <= nc < n):  # only update when it is found that the neighboring cell can be reached with a shorter distance
                    if distances[nr][nc] > distances[r][c] + 1:
                        distances[nr][nc] = distances[r][c] + 1
                        queue.append((nr, nc))
        return distances




