class Solution:

    """
    Strategy: Sorting 
    Time Compelxity: O(nlogn)
    Space Complexity: O(n)
    """
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        # time complexity: o(nlogn) | TimeSort
        sorted_s = sorted(s)

        # time complexity: o(nlogn) | TimeSort
        sorted_t = sorted(t)


        # time complexity: o(n) | Loop over array with lenght n
        for index in range(len(s)):
            if sorted_s[index] != sorted_t[index]:
                return False
        else:
            return True
                    

            