class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]
        maximum=max(candies)
        for i in candies:
            extra=i+extraCandies
            if extra>=maximum:
                output.append(True)
            else:
                output.append(False)  
        return output
