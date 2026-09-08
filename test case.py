class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums=[2,7,11,15]
        target=9
        rlist=[]
        for i in range(nums):
            b= i+1
            if i + b == target :
                rlist.append(i,b)
            else:
                print("Hell")

