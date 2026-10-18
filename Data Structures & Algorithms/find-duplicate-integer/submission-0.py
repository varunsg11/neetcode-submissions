class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapp = {}

        for i in nums:
            if i in mapp:
                return i
            else:
                mapp[i] = i