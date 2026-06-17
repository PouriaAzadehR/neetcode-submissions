class Solution:

    """
    Strategy: Sorting
    Time Complexity: o(m*n*logn) 
    Space Complexity: o(n*m)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # keys: sorted string | values: [string, string]
        # space complexity: o(m*n)
        dict_sorted_string_to_strs = dict() 


        # time complexity: o(m*nlogn)
        for string in strs:

            # time complexity: o(nlogn) | time sort algorithm 
            sorted_string = sorted(string)

            # time complexity: o(1) | look up with hash funciton
            if str(sorted_string) not in dict_sorted_string_to_strs.keys():
                dict_sorted_string_to_strs[str(sorted_string)] = [string]
            else:
                dict_sorted_string_to_strs[str(sorted_string)].append(string)
        
        

        result_list = list()

        # time complexity: o(n) 
        for value in dict_sorted_string_to_strs.values():
            # time complexity: o(1)
            result_list.append(value)

        return result_list
