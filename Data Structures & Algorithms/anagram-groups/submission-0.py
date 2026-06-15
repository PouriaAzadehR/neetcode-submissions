class Solution:

    """
    Strategy: HashMaps(Dictionaries)
    Time Complexity: o(n*n*m) 
    Space Complexity: o(n*m)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        list_dictionary_strs = list()

        # time complexity: o(n*m)
        for string in strs:
            # time complexity: o(m)
            string_dictionary = dict()

            for character in string:
                if character not in string_dictionary.keys():
                    string_dictionary[character] = 1
                else:
                    string_dictionary[character] += 1
                
            list_dictionary_strs.append({string:string_dictionary})

        result = list()

        # time complexity: o(n)
        for outer_loop_index in range(len(list_dictionary_strs)):
            if list_dictionary_strs[outer_loop_index] == None:
                continue
            sublist_result = [list(list_dictionary_strs[outer_loop_index].keys())[0]]

            # time complexity: o(n)
            for inner_loop_index in range(outer_loop_index + 1, len(list_dictionary_strs)):
                if list_dictionary_strs[inner_loop_index] == None:
                    continue
                
                # time complexity: o(m)
                if list(list_dictionary_strs[outer_loop_index].values())[0] == list(list_dictionary_strs[inner_loop_index].values())[0]:
                    sublist_result.append(list(list_dictionary_strs[inner_loop_index].keys())[0])
                    list_dictionary_strs[inner_loop_index] = None
            list_dictionary_strs[outer_loop_index] = None
            result.append(sublist_result)
        


        return result
