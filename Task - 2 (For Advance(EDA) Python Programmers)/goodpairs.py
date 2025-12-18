from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq = {}
        for num in nums:
            if num in freq:
                count += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1
        return count

s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))
print(s.numIdenticalPairs([1,1,1,1]))
print(s.numIdenticalPairs([1,2,3]))
