class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            if nums[i] == val:
                nums[i] = nums[j]
                nums[j] = '_'
                k = k + 1
                i = i - 1
                j = j - 1
            i = i + 1
        return len(nums) - k