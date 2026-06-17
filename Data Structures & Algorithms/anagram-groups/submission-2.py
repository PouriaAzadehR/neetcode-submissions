class Solution:

    """
    Strategy: Creating Identity With ASCII Codes
    Time Complexity: o(m*n) 
    Space Complexity: o(n*m)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_ASCII_string = dict()

        # time complexity: o(m*n)
        for string in strs:
            ascii_identity = [0] * 26

            # time complexity: o(m)
            for character in string:
                ascii_index = ord("a") - ord(character)
                ascii_identity[ascii_index] += 1

            dict_ASCII_string.setdefault(tuple(ascii_identity), []).append(string)
        

        result_list = list()

        for value in dict_ASCII_string.values():
            result_list.append(value)
        return result_list