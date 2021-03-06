"""
88. Merge Sorted Array
Easy

2243

228

Add to List

Share
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?


EXPLORE THIS SOLUTION IN THE FUTURE:

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        c1, c2 = m-1, n-1
        for i in reversed(range(m+n)):
            if c1 >= 0 and (c2 < 0 or nums1[c1] > nums2[c2]):
                nums1[i] = nums1[c1]
                c1 -= 1
            else:
                nums1[i] = nums2[c2]
                c2 -= 1


"""
#####################
# Runtime: 20 ms, faster than 90.25% of Python online submissions for Merge Sorted Array.
# Memory Usage: 13.6 MB, less than 19.13% of Python online submissions for Merge Sorted Array.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        if (len(nums1) != m + n) or (len(nums2) != n) or (1 > m + n > 200):
            return
        
        # if m is 0 then copy the whole nums2 in nums1
        if m == 0 and n > 0:
            for i, num in enumerate(nums2): # from zero to m+n
                nums1[i] = num
            return nums1

        # if nums2 is empty return only nums1
        if m > 0 and n == 0:
            return nums1

        index1 = 0
        index2 = 0
        index_insert = 0
        
        copy_nums1 = []
        for num in nums1:
            copy_nums1.append(num)
        # copy_nums1 = nums1.copy()

        while index1 < m and index2 < n:
            if copy_nums1[index1] <= nums2[index2]:
                nums1[index_insert] = copy_nums1[index1]
                index_insert += 1
                index1 += 1

            elif copy_nums1[index1] > nums2[index2]:
                nums1[index_insert] = nums2[index2]
                index_insert += 1
                index2 += 1

        # nums1 is all at the place and still need to check nums2 and instert in nums1
        if m == index1:
            while index2 < n:
                nums1[index_insert] = nums2[index2]
                index_insert += 1
                index2 += 1

        if n == index2:
            while index1 < m:
                nums1[index_insert] = copy_nums1[index1]
                index1 += 1
                index_insert += 1
       # print(nums1)

        return nums1


             


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)

