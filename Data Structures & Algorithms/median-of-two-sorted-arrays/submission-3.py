class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        total = len(nums1) + len(nums2)
        A = nums1
        B = nums2
        if len(A) > len(B):
            A , B = B , A

        half = total//2
        left = 0
        right = len(A) - 1
        while True:
            mid = (left + right) // 2 if left <= right else -1
            b_mid = half - (mid + 1 ) - 1

            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid + 1] if mid + 1 < len(A) else float("infinity")
            Bleft = B[b_mid] if b_mid >= 0 else float("-infinity")
            Bright = B[b_mid + 1] if b_mid + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return float(min(Aright , Bright))
                else:
                    return (max(Aleft,Bleft) + min(Bright,Aright))/2
            elif Aleft > Bright:
                right = mid - 1
            else:
                left = mid + 1