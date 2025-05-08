class Solution(object):
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        running_sum_array = []

        for index, value in enumerate(nums):

            if index == 0:
                running_sum_array.append(value)

            elif index < len(nums):
                running_sum_array.append(running_sum_array[index-1] + value)

        return running_sum_array


nums1 = [1,2,3,4]
nums2 = [1,1,1,1,1]
nums3 = [3,1,2,10,1]

sol1 = Solution()
print(sol1.runningSum(nums1))