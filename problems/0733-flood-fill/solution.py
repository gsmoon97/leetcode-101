from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        queue = deque([(sr, sc)])  # BFS queue (FIFO)
        ocolor = image[sr][sc]
        if ocolor == color:
            return image  # early termination when the target pixel does not need to be updated

        offsets = [(-1,0), (1,0), (0,-1), (0,1)]
        while queue:
            nr, nc = queue.popleft()
            ncolor = image[nr][nc]
            if ncolor != ocolor:
                continue
            
            image[nr][nc] = color
            for offset_r, offset_c in offsets:  # iterate over adjacent pixels
                offr = nr + offset_r
                offc = nc + offset_c
                if ((0 <= offr < M) and (0 <= offc < N)):
                    queue.append((offr, offc))
        return image