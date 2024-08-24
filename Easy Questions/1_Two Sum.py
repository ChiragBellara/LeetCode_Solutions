# IMPORTS
from typing import List


# BRUTE FORCE --> Time Complexity: O(n^2)
# We simply iterate over the entire list, checking for every pair of numbers
# As soon as we get a pair that sums to the target, we return.
# Since the question states that there will always be atleast one answer,
# we do not need to handle the case where the pair is not found.
def twoSum(self, nums: List[int], target: int) -> List[int]:
    N = len(nums)
    for i in range(N):
        for j in range(i+1, N):
            if nums[i] + nums[j] == target:
                return [i, j]


# OPTIMIZED --> Time Complexity: O(n) but uses additional space O(n)
# We mantain a hashmap, which keeps a track of what number have we
# seen till now. At every step, we find the difference between the current
# number and the target, and we check if this difference is present in the hash map.
# If it is, we return the index from the hash map and the index of the current number.
# If it is not, we add this number to the hashmap along with it's index.
def twoSum(self, nums: List[int], target: int) -> List[int]:
    N = len(nums)
    seen = {}

    for i, val in enumerate(nums):
        diff = target - val
        if diff in seen:
            return [i, seen[diff]]
        seen[val] = i
