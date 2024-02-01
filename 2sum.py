class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        while count < len(nums):
            sub = target - nums[count]
            if (sub in nums) and (nums.index(sub) != count):
                result = [count, nums.index(sub)]
                return result
            else:
                count += 1


Solution().twoSum([2, 7, 11, 15], 9)
