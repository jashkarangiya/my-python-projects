# class Solution:
#     def removeDuplicates(self, nums):
#         nums[:] = set(nums)
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        nums.sort()
        print(nums)
        while i != len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        # print(len(nums))
        return len(nums)

    # def bubbleSort(list2, numberOfElements):
    #
    #     for i in range(numberOfElements):
    #         for j in range(numberOfElements - 1):
    #             if list2[j] < list2[j + 1]:
    #                 temp = list2[j]
    #                 list2[j] = list2[j + 1];
    #                 list2[j + 1] = temp;
    #     return 0

nums = []
length = int(input())
for i in range(length):
    elements = int(input())
    nums.append(elements)
print(nums)

# nums = [1, 1, 2, 3, 1, 0 , 5, 2]
# Solution.bubbleSort(nums, len(nums))
print(nums)
result = Solution.removeDuplicates(0,nums)
print(result)


