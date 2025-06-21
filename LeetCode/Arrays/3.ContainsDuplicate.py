# EASY

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

#     1 <= nums.length <= 105
#     -109 <= nums[i] <= 109

def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = Counter(nums)
        for i in d:
            if d[i]>1:
                return True
        return False
    
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = Counter(nums)
        for k,v in d.items:
            if v>1:
                return True
        return False
    
def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)
        if len(s) != len(nums):
            return True
        return False

def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
                return True
            else:
                d[nums[i]] = 1
        return False
