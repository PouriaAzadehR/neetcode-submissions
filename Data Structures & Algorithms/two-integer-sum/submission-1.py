class Solution:



    """
    Strategy: Hash Tables
    Time Complexity: o(n)
    Space Complexity: o(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # numbers -> indexes
        nums_frequnices = dict()

        # time complexity: o(n)
        for index in range(len(nums)):
            if nums[index] not in nums_frequnices.keys():
                nums_frequnices[nums[index]] = [index]
            else:
                nums_frequnices[nums[index]].append(index)
        

        # time complexity: o(n)
        for key in nums_frequnices.keys():
            first_index = 0
            second_index = 0
        
            candidate_pair_key = target - key

            # time complexity: o(1)
            if candidate_pair_key in nums_frequnices.keys():
                if key != candidate_pair_key:
                    return [nums_frequnices[key][0], nums_frequnices[candidate_pair_key][0]]
                else:
                    if len(nums_frequnices[key]) >= 2:
                        return nums_frequnices[key][0:2]
            
        

        
        