


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count=[]
        for i in range(0,len(nums)-1):
            if nums[i]!=nums[i+1]:
                count.append(nums[i])
            i=i+1
        return count



result=Solution()

print(result.removeDuplicates([1,1,2,2,5,3]))