class Solution:
    # Design: 
    # Use a Set to keep track of the currently seen characters.
    # Progress the right index through the string adding each character seen to the Set, and increasing the max length tracker.
    # When we come across a duplicate character, progress the left index removing each character passed from the Set.
    # Once we pass the duplicate character, progress the left index once more, but without removing the duplicate, since it is contained by the right index.
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftIndex = 0
        charSet = set()
        maxLength = 0

        for rightIndex in range(len(s)):
            # if the character is new add the character to the set and increase the length if it's larger than the current max
            if not s[rightIndex] in charSet:
                charSet.add(s[rightIndex])
                maxLength = max(maxLength, rightIndex - leftIndex + 1)
            else:
                # otherwise we hit a character so progress left index to the index past the match
                while(s[leftIndex] is not s[rightIndex]):
                    charSet.remove(s[leftIndex])
                    leftIndex += 1
                # Move once more to progress past the character, but don't that character from the set
                leftIndex += 1

        return maxLength
    
# Post Analysis
# Nothing of note, just be careful of that index difference on the max
# Glad I thought of the leftIndex moving once more, that could have been a pain to debug