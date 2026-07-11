class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ls = nums1 + nums2
        sortedLs = sorted(ls)
        l , r = 0, len(sortedLs) - 1
        if len(sortedLs) % 2 == 0:
            return (sortedLs[(l + r) // 2] + sortedLs[((l + r) // 2) + 1]) / 2
        else:
            return sortedLs[(l + r) // 2]



