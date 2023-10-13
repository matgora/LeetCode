class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        k = 0
        i = 0
        best = 0
        while i < len(nums):
            if s >= target:
                if best == 0 or best > k:
                    best = k
                s = s - nums[i-k]
                k = k - 1
            else:
                s = s + nums[i]
                k = k + 1
                i = i + 1
        while s >= target:
            if best == 0 or best > k:
                best = k
            s = s - nums[i-k]
            k = k - 1
        return best