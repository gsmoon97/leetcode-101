class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # DP is more suitable for counting/checking existence
        # Backtracking is more suitable for this type of problem since the task is to find all possible combinations
        all_combinations = []

        def backtrack(remaining_target, combinations, start_idx):  # helper function to backtrack all possible sub-combinations
            if remaining_target < 0:  # invalid combination
                return
            if remaining_target == 0:  # valid combination
                all_combinations.append(combinations.copy())  # copy() the list to prevent mutating the shared list
                return
            for i in range(start_idx, len(candidates)):  # add more numbers to find valid combination that sum upto `target`
                combinations.append(candidates[i])  # try building combination initialized with the current candidate as the first element
                backtrack(remaining_target - candidates[i], combinations, i)  # `start_idx` to prevent duplicates
                combinations.pop()  # backtracks
            return combinations
        
        backtrack(target, [], 0)
        return all_combinations