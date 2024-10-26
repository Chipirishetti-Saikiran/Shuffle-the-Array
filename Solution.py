class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        k=len(nums)//2 
        suf=[] 
        for i in range(k):
            suf.append(nums[i])
            suf.append(nums[i+k]) 
        return suf    

        
