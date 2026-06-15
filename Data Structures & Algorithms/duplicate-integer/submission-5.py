class Solution:


    """ 
        Name: Brute Force, Nested Loop 
        Time Complexity: o(n * n)
        Space Complexity: o(1)
    """
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Nested Loop: Time Complexity: O(n*n)
        for number in nums:
            # Space Complexity:O(1)
            frequency = 0

            for number_iterator in nums:
                if number == number_iterator:
                    frequency += 1
            
            if frequency >= 2:
                return True

        else:
            return False


    """
        Name: Hash Maps
        Time Complexity: O(n)
        Space Complexity: O(n) 
    """
    def hasDuplicate(self, nums: List[int]) -> bool:

        # space complexity: o(n)
        presence_of_numbers = dict()

        # time complexity: o(n)
        for number in nums:
            # dictionary lookup: o(1) | hash functions
            if presence_of_numbers.get(number) == None:
                presence_of_numbers[number] = True
            else:
                return True

        else:
            return False

    """
        Name: Hash Sets
        Time Complexity: O(n)
        Space Complexity: O(n) 
    """
    def hasDuplicate(self, nums: List[int]) -> bool:

        # space complexity: o(n)
        presence_of_numbers = set()

        # time complexity: o(n)
        for number in nums:

            # set lookup: o(1) | hash functions
            if number in presence_of_numbers:
                return True
            else:
                presence_of_numbers.update(number)

        else:
            return False


    """
    Strategy: Sorting
    Time Complexity; o(nlogn)
    Space Complexity: o(n) 
    """
    def hasDuplicate(self, nums: List[int]) -> bool:


        # time complexity: o(nlogn) | Time Sort
        sorted_nums = sorted(nums)

        print(sorted_nums)

        # time complexity: o(n)
        for index in range(len(sorted_nums)-1):
            if sorted_nums[index] == sorted_nums[index+1]:
                return True
        else:
            return False

            

        