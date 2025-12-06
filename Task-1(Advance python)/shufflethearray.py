class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]      # first n elements
        y = nums[n:]      # last n elements
        result = []
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
        return result
