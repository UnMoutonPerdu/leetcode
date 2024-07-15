class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cloneSet = set()
        for num in nums:
            if num in cloneSet:
                return True
            cloneSet.add(num)
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))