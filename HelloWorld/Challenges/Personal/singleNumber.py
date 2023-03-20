# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#       count = 0
#       nums.sort()
#       # print(nums)
#
#       for i in range(len(nums) - 1):
#         # if i < len(nums):
#           if nums[i] == nums[i + 1]:
#             count= count + 1
#           else:
#             print(nums[i])
#         else:
#           break;