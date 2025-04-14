class Solution:
    '''
    Design:
        What makes a palindrome a palindrome? A seed starting with either xx or xyx and expanding out from there.
        Find all sets of xx or xyx and determine which is the longest.
        2 Parts: Find Seeds and Find Lengths
        1. Find Seeds
            Loop:
                For each index that matches the index + 1, add it to an array of off-centered seeds
                For each index that matches the index + 2, add it to an array of centered seeds
        2. Find Lengths
            Loop:
                For a given index1 and index2, if the values of index1 - 1 and index2 + 1 are equal, expand and continue
                Return the final value of index1 as it is the start of the palindrome and index2 - index1 + 1 as the length of the palindrome
            Do this loop for both off-centered and centered seeds
        When a given return of the lengths loop is greater than a previous one, store the start index and length of that palindrome
        Return string from start index to start index + length        
    '''
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return s

        # 1. Find Seeds
        centerSeedArray, offcenterSeedArray = self.findSeeds(s, length)

        # For Offcenter, take the median array in a run of numbers
        offcenterSeedArray = self.removeRunsOfPalindromes(offcenterSeedArray)
        centerSeedArray = self.removeRunsOfPalindromes(centerSeedArray)

        # 2. Find Palindrome Lengths
        maxLength = 0
        maxIndex = 0
        for seed in centerSeedArray:
            seedLength, seedIndex = self.findPalindromeLength(s, length, seed, seed + 2)
            if seedLength > maxLength:
                maxLength = seedLength
                maxIndex = seedIndex

        for seed in offcenterSeedArray:
            seedLength, seedIndex = self.findPalindromeLength(s, length, seed, seed + 1)
            if seedLength > maxLength:
                maxLength = seedLength
                maxIndex = seedIndex

        return s[0] if maxLength == 0 else s[maxIndex:(maxIndex + maxLength)]
        
    # Find Starting Seeds of palindromes
    def findSeeds(self, s: str, length: int):
        centerSeedArray = []
        offcenterSeedArray = []
        for index in range(length - 1):
            # If the value matches the next value, it's offcentered seed "xx"
            if s[index] == s[index + 1]:
                offcenterSeedArray.append(index)
            
            # If the value matches the next, next value, it's a centered seed "xyx"
            if index < (length - 2) and s[index] == s[index + 2]:
                centerSeedArray.append(index)

        return centerSeedArray, offcenterSeedArray
    
    # Find the length of each palindrome seed, expanding out from the center until it's no longer a palindrome
    def findPalindromeLength(self, s: str, length: int, index1: int, index2: int):
        start = index1
        end = index2
        while start > 0 and end < (length - 1) and s[start - 1] == s[end + 1]:
            start -= 1
            end += 1

        return (end - start + 1), start
    
    # Remove any runs in the list of palindrome seed list and keep the median seed of the run
    def removeRunsOfPalindromes(self, startingArray: [int]):
        startRun = -1
        endRun = -1

        # Look for runs
        for i in range(len(startingArray) - 1):
            # Found a run
            if startingArray[i] == (startingArray[i + 1] - 1):
                if startRun == -1:
                    startRun = i
                endRun = i + 1

            # Run ended
            if startingArray[i] != (startingArray[i + 1] - 1) or i == (len(startingArray) - 2):
                if startRun != -1:
                    for j in range(startRun - endRun):
                        # Remove all values except the median entry
                        if j != (startRun - endRun) // 2:
                            startingArray[startRun + j].remove()
                    i = startRun
                    startRun = -1
                    endRun = -1

        return startingArray

# Test Locally    
# Solution().longestPalindrome("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
'''
Post Analysis
    - Expanding out can take too long for every seed identified, given that duplicate palindromes can be found, 
    it's safe to remove all runs of palindromes and keeping the median array as the largest. Although I haven't 
    tested this to be exhaustive, I'm guessing there are corner cases.
    - It seems like there is probably some additional removals that could be done. If your max is large enough,
    and the next index is too close, obviously that index will fail to produce a large enough palindrome.
    - Even though this got a quite good score on LeetCode (beat 67.57%), it feels like there is probably an
    additional trick here. It also uses a fair amount of memory. I did sacrifice performace/capacity to allow
    for the code to be more easily understood and cleaner to read.
'''

