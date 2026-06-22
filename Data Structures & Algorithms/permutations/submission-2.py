class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     possible_permutations = []

    #     def dfs(candidate, remaning_choices):

    #         copy_candidate = candidate[:]

    #         if len(copy_candidate) == len(nums):
    #             possible_permutations.append(copy_candidate)
    #             return

    #         new_remaning_choices = remaning_choices[:]
    #         for i_choice in range(len(remaning_choices)):
    #             copy_candidate.append(remaning_choices[i_choice])
    #             new_remaning_choices.pop(i_choice)
    #             dfs(copy_candidate, new_remaning_choices)

    #             new_remaning_choices = remaning_choices[:]
    #             copy_candidate = candidate[:]

    #         return

    #     dfs([], nums)

    #     return possible_permutations

    def permute(self, nums: List[int]) -> List[List[int]]:

        possible_permutations = [[nums[0]]]

        for new_number in nums[1:]:
            tepm = []
            for each_permuation in possible_permutations:
                for item_index in range(len(each_permuation)+1):
                    copy_each_permuation = each_permuation[:]
                    copy_each_permuation.insert(item_index, new_number)
                    tepm.append(copy_each_permuation)
            possible_permutations.extend(tepm)


        final = [item for item in possible_permutations if len(item) == len(nums)]

        return final
