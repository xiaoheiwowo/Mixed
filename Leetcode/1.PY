class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenth = len(nums)
        li = list()
        for i in nums:
            for j in nums:
                if nums.index(j) > nums.index(i):
                    li.append(i+j)

        # print(li)
        if target in li:
            count = li.index(target)
        a = b = 0
        for i in range(lenth-1):
            count -= (lenth - 1 - i)
            if count < 0:
                a = i
                b = nums.index(target - nums[a])
                break

        return [a, b]



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target - nums[j] == nums[i]:
                    return [i, j]
                


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([2, 2, 7, 11, 15, 33, 44, 55, 66, 77], 4))