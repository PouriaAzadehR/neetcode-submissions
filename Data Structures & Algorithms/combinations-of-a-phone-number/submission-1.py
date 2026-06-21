class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digits_to_letters = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        output_combination = [[""]]

        if digits == "":
            return []

        for i in range(len(digits)):
            letter_combintation = []
            for letter in digits_to_letters[int(digits[i])]:
                for existing_combintation in output_combination[i]:
                    letter_combintation.append(existing_combintation + letter)
            output_combination.append(letter_combintation)

        
        return output_combination[len(digits)]
