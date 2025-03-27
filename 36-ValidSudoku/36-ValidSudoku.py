# Last updated: 3/26/2025, 10:29:48 PM
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                current = n
                while (current + 1) in numSet:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest     