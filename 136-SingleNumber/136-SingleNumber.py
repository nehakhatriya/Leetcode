class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # hashmap={}

        # for i in nums:
        #     if i in hashmap:
        #         del hashmap[i]
        #     else:
        #         hashmap[i]=0
        # return list(hashmap)[0]

        result=0
        for i in nums:

            result=result^i
        return result