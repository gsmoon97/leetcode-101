class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        N = len(nums)
        permutations = []
        def backtrack(permutation: List[int], used: List[bool]):
            if len(permutation) == N:
                permutations.append(permutation.copy())
                return
            for i in range(N):
                if used[i]:  # check if current number has been used already
                    continue
                
                # choose the current number
                permutation.append(nums[i])
                used[i] = True
                
                # explore all possible sub-permutations
                backtrack(permutation, used)
                
                # backtrack the current number for the next iteration
                permutation.pop()
                used[i] = False
            return

        backtrack([], [False] * N)  # initialize
        return permutations