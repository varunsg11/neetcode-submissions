class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res = sorted(res)

        mid =  len(res) // 2

        if len(res) % 2 == 0:
            return (res[mid] + res[mid -1]) / 2
        return res[mid]