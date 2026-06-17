class Solution:


    # strategy: brute force
    # time complexity: o(k*n*n)
    # space complexisty: o(k)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        k_most_frequent_numbers = list()
        
     
    ################################ Frequency Counter ################################
    
        # key: number in the list | value: frequency
        dict_frequency_numbers = dict()

        # time complexity: o(n*n)
        for outer_num_index in range(len(nums)):
            frequency = 0
            for inner_num_index in range(len(nums)):
                if nums[outer_num_index] == nums[inner_num_index]:
                    frequency += 1
            
            if nums[outer_num_index] not in dict_frequency_numbers.keys():
                dict_frequency_numbers[nums[outer_num_index]] = frequency

        
    ################################ Top K Selecting ################################

        k_most_frequent = list()

        # time complexity: o(k*n)
        for k_index in range(k):
            candidate_key, candidate_value = -1001, -1001

            for key, value in dict_frequency_numbers.items():
                if value > candidate_value:
                    candidate_key, candidate_value = key, value

            k_most_frequent.append(candidate_key)
            dict_frequency_numbers.pop(candidate_key)

        return k_most_frequent


