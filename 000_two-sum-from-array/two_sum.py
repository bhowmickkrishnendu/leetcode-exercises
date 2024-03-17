class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))