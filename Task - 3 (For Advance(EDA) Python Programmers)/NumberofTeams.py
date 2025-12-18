from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        for j in range(n):
            left_smaller = left_greater = 0
            right_smaller = right_greater = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    right_greater += 1
                else:
                    right_smaller += 1
            count += left_smaller * right_greater
            count += left_greater * right_smaller
        return count

s = Solution()
print(s.numTeams([2,5,3,4,1]))
print(s.numTeams([2,1,3]))
print(s.numTeams([1,2,3,4]))
