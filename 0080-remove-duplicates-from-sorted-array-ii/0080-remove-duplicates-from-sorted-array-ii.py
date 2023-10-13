class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        counter = 0
        while fast < len(nums) - 1:
            if nums[fast] == nums[fast+1]:
                counter = counter + 1
                if counter < 2:
                    slow = slow + 1
            else:
                slow = slow + 1
                counter = 0
            nums[slow] = nums[fast + 1]
            fast = fast + 1
        return slow + 1