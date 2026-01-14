class Solution:
    def sortColors(self,nums):
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if(nums[i]>nums[j]):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        """
        Do not return anything, modify nums in-place instead.
 
       """
        return nums
n=int(input())
nums=list(map(int,input().split()))
s=Solution()
print(s.sortColors(nums))