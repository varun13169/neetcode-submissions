class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        
        total = m + n
        half = total // 2
        if total%2 != 0:
            half = half + 1
        
        for i in range(0, m+1):
            j = (half) - i
            print(i, j, half, total)

            L1 = nums1[i-1] if i > 0 else float('-inf')
            L2 = nums2[j-1] if j > 0 else float('-inf')

            R1 = nums1[i] if i < m else float('inf')
            R2 = nums2[j] if j < n else float('inf')
            print(L1, L2, R1, R2)

            if L1 <= R2 and L2 <= R1:
                if total%2 != 0:
                    return max(L1, L2)
                else:
                    return ( max(L1, L2) + min(R1, R2) ) / 2
