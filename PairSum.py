# Find pairs in a sorted list that sums to given number. 
# If not found return an empty list

from typing import List

#nums, target = [0, 5 ,6, 9], 11

# Brute force O(n^2)
def brute_force(nums: List[int], target: int) -> List[int]:
    
    n = len(nums)
    result = []

    for i in range(n):
        for j in range(i+1, n):
            if (nums[i] + nums[j]) == target:
                result.append([i,j])
    
    return result

# Single pass O(n)
def inward_run(nums: List[int], target: int) -> List[int]:
    
    left, right = 0, len(nums)-1
    result = []

    while left<right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        elif sum == target:
            result.append([left, right])
            left += 1
    
    return result
            


nums = list(map(int, input("Type numbers with space for list: ").split()))

target = int(input("Type target sum number: "))

#print(brute_force(nums, target))
print(inward_run(nums, target))

