class Solution(object):
    def runningSum(self, nums: list[int]) -> list[int]:

        running_sum_array = [0] * len(nums)
        running_sum_array[0] = nums[0]

        for index in range(1, len(nums)):

            running_sum_array[index] = nums[index] + running_sum_array[index - 1]

        return running_sum_array


nums1 = [1,2,3,4]
nums2 = [1,1,1,1,1]
nums3 = [3,1,2,10,1]

sol1 = Solution()
print(sol1.runningSum(nums1))