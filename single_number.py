class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        new_dict=dict()
        for num in nums:
            new_dict[num]=new_dict.get(num,0)+1
            #print(new_dict)

        for key,value in new_dict.items():
            if value==1:
                print(key)
                break


solution=Solution()
solution.singleNumber([2,2,1])