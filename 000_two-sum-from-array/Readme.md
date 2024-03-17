
# Efficient Two Sum Solution using Dictionary in Python



## Intuition

The first thought that came to my mind was to iterate through the list of numbers and check if the complement of each number (target - num) exists in the list. If it does, we can return the indices of the two numbers that sum up to the target.


## Approach

To implement this idea, I decided to use a dictionary to store the numbers and their indices as I iterate through the list. This way, I can check if the complement of the current number is already in the dictionary. If it is, I can return the indices of the current number and its complement. If not, I add the current number and its index to the dictionary and continue the iteration.
## Complexity


**Time complexity:** O(n), where n is the length of the input list nums. We iterate through the list once, performing constant-time operations (dictionary lookups and insertions) for each element.


**Space complexity:** O(n), where n is the length of the input list nums. In the worst case, we might need to store all the numbers in the dictionary, which requires O(n) space.
## Code


```bash
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
```

