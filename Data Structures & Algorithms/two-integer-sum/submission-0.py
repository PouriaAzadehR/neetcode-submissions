class Solution:



    """
    Strategy: Brute Force | Nested Loops
    Time Complexity: o(n*n)
    Space Complexity: o(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # time complexity: o(n*n)
        for outer_loop_index in range(len(nums)):
            for inner_loop_index in range(outer_loop_index + 1, len(nums)):
                if nums[outer_loop_index] + nums[inner_loop_index] == target:
                    return [outer_loop_index, inner_loop_index]
        
        