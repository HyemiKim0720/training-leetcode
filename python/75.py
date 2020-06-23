# 75. Sort Colors
#
# Wrong answer
# counting process: fail solution: Runtime Error
# if dic don't have value '1', dic can't dic.get(1)

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         dic={}
#         for i in nums:
#             if i not in dic:
#                 dic[i]=nums.count(i)
#         rewi=dic.get(0)
#         wibl=dic.get(1)
        
#         for i in range(len(nums)):
#             if i<rewi:
#                 nums[i]=0
#             elif i>=(rewi+wibl):
#                 nums[i]=2
#             else:
#                 nums[i]=1
#
#
#
# Correct answer
# counting process 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[0,0,0]
        for i in nums:
            if l[i]==0:
                l[i]=nums.count(i)
        
        for i in range(len(nums)):
            if i<l[0]:
                nums[i]=0
            elif i>=(l[0]+l[1]):
                nums[i]=2
            else:
                nums[i]=1
