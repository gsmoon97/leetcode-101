class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # naive approach: try all the possible scenarios i.e., backtrack
        # backtrack consists of 3 stages: 1) choose 2) explore 3) un-choose
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        R, C = len(board), len(board[0])

        def backtrack(row, col, index):
            # base case (i.e., reached all the characters in the word)
            if index == len(word):
                return True

            # invalid cases (out-of-bound indices, character mismatch)
            if 0 > row or row >= R or 0 > col or col >= C or board[row][col] != word[index]:
                return False
            
            # choose
            temp = board[row][col]
            board[row][col] = '#'  # use hashtag (#) to mark visited cells

            # explore the four directions
            for move_row, move_col in directions:
                new_row, new_col = row + move_row, col + move_col            
                if backtrack(new_row, new_col, index + 1):
                    return True
                
            # un-choose
            board[row][col] = temp
            return False

        # call `backtrack` only when the cell matches the first character of the word
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if backtrack(r,c, 0):
                        return True
        return False
