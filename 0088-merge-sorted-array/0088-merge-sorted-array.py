class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        j = 0
        num2 = nums2[j]
        zero_pos = m
        for i in range(m+n):
            num1 = nums1[i]
            if not(num1 == 0 and i >= zero_pos) and num1 <= num2:
                continue
            elif num1 > num2:
                for x in reversed(range(i+1, zero_pos+1)):
                    nums1[x] = nums1[x-1]
                zero_pos = zero_pos + 1
            nums1[i] = num2
            j = j + 1
            if j == n:
                 break
            num2 = nums2[j]