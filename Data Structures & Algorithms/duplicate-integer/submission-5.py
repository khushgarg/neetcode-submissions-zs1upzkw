class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ONE = set()
        for n in nums:
            if n in ONE:
                return True
            ONE.add(n)
        return False


        
        