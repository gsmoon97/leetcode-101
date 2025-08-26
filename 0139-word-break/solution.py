class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}  # memoization to ensure each unique substring is checked only once
        
        # top-down dynamic programming with memoization
        def dp(s: str) -> bool:
            if not s:
                return True
            
            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1):
                subword = s[:i]
                if subword in wordDict:
                    if dp(s[i:]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        
        return dp(s)