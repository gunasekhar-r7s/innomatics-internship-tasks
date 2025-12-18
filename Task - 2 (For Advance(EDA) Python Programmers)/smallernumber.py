from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result

s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))
print(s.smallerNumbersThanCurrent([6,5,4,8]))
print(s.smallerNumbersThanCurrent([7,7,7,7]))
