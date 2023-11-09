class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = []
        previous = 0
        for elem in nums:
            runSum.append(elem + previous)
            previous = runSum[-1]

        return runSum 