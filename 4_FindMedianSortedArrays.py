# Repo Only
from typing import List

# LeetCode
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Design:
        # Simple way is to sort into one array and take the middle number if whole, otherwise the average of the middle two numbers
        # Easy in python, just combine them and sort, then find the middle
        # If the length is even, take the middle 2 values, (shove into int to floor)
        # Otherwise, take the middle value

        combinedNums = nums1 + nums2
        combinedNums.sort()
        length = len(combinedNums)
        middleIndex = length // 2

        if (length % 2) == 0:
            # When Even, get middle two values
            return (combinedNums[middleIndex - 1] + combinedNums[middleIndex]) / 2
        else:
            # When Odd, get middle value
            return combinedNums[middleIndex]

# Post Analysis:
# Over thought this one
# Needed to use combinedNums instead of middleIndex for if statement
# While len(combinedNums) // 2 gets us the floored value, since we use len, it's the value one above the middle, not below the mdidle.
# Was able to reduce runtime by only getting the length once.
