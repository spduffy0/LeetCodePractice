# Repo Only
from typing import List

# LeetCode

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Design:
        # Could just loop through twice, but that will get expensive for long lists
        # Store the value and it's index in a dictionary as a key, value, pair and use math to calculate if we have the compliment in the list.
        # Since each value is used only once, we just add elements into the dictionary until we find a match.
        # Loop: - will need index as well, enumberate
        #   If the (target - value) is in the dictionary return value for that entry and the current index [value, index].
        #   Otherwise add the value, index pair to the dictionary.
        numbers = dict()

        for index, currentNumber in enumerate(nums): 
            if currentNumber in numbers:
                return [numbers[currentNumber], index]
            else:
                numbers[target - currentNumber] = index

        return []

# Post Analysis:
# I was wanting to check for the difference in the if statement, but the difference only gets stored as the key, later on the difference is the current number