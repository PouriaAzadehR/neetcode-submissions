class Solution:
    """
    Strategy: Dictionaries(HashTables)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # space complexity: o(n)
        s_characters_frequence = dict()
        # space complexity: o(n)
        t_characters_frequence = dict()

        # time complexity: o(n)
        for character in s:
            # time complexity: o(1) | look up with hash funcitons
            if character not in s_characters_frequence.keys():
                s_characters_frequence[character] = 1
            else:
                s_characters_frequence[character] += 1

        # time complexity: o(n)
        for character in t:
            # time complexity: o(1) | look up with hash funcitons
            if character not in t_characters_frequence.keys():
                t_characters_frequence[character] = 1
            else:
                t_characters_frequence[character] += 1

        if len(s_characters_frequence.keys()) != len(t_characters_frequence.keys()):
            return False

        for s_key in s_characters_frequence.keys():
            if s_key not in t_characters_frequence.keys():
                return False

            if s_characters_frequence[s_key] != t_characters_frequence[s_key]:
                return False

        else:
            return True
