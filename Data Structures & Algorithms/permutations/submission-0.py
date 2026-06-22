class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        possible_permutations = []



        def dfs(candidate, remaning_choices):

            copy_candidate = candidate[:]

            if len(copy_candidate) == len(nums):
                possible_permutations.append(copy_candidate)
                return
            
            new_remaning_choices = remaning_choices[:]
            for i_choice in range(len(remaning_choices)):
                
                copy_candidate.append(remaning_choices[i_choice])
                new_remaning_choices.pop(i_choice)
                dfs(copy_candidate, new_remaning_choices)

                new_remaning_choices = remaning_choices[:]
                copy_candidate = candidate[:]


            
            return

        dfs([], nums)

        return possible_permutations
