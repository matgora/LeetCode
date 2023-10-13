class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 1
        val = nums[0]
        while i < len(nums):
            if nums[i] == val:
                nums[i-1] = 101
                k = k + 1
            i = i + 1
            val = nums[i-1]
        nums.sort()
        return len(nums) - k