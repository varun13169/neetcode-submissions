class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        lenN1 = len(nums1)
        lenN2 = len(nums2)

        total = lenN1 + lenN2
        isTotalEven = total % 2 == 0
        mid = total // 2
        if not isTotalEven:
            mid = mid+1


        lo = 0
        hi = lenN1
        while lo <= hi:
            i = lo + ((hi-lo) // 2)
            j = mid - i

            L1 = nums1[i-1] if i > 0 else float("-inf")
            R1 = nums1[i] if i < lenN1 else float("inf")
            L2 = nums2[j-1] if j > 0 else float("-inf")
            R2 = nums2[j] if j < lenN2 else float("inf")

            if L1 <= R2 and L2 <= R1:
                if isTotalEven:
                    # print(R1, R2, L1, L2, i, j)
                    return ( min(R1, R2) + max(L1, L2) ) / 2
                else:
                    return max(L1, L2)
            
            if L1 > R2:
                hi = i - 1
            else:
                lo = i + 1
            
        