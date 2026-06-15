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


            

        