class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #nums = [1,2,3,1]
        valores = set()


        for i in nums:
            if i in valores:
                return True
            valores.add(i)
        return False
    
            
input = [1,2,3,4,1]
sol = Solution()
print(sol.containsDuplicate(input))