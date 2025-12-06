class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=[]
        total=0
        for i in nums:
            total+=i
            runningSum.append(total)
        return runningSum
