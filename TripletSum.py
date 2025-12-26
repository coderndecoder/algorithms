# Find triplets from list of integers that sum to 0. No duplicates.
# a + b + c = 0

from typing import List, Set

# brute force 
def brute_force(nums: List[int]) -> List[List[int]]:
    
    n = len(nums)
    triplets = set()
    
    for i in range(n):
     for j in range(i+1, n):
         for k in range(j+1, n):
            if(nums[i] + nums[j] + nums[k] == 0):
                triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
            
            
    return [list(t) for t in triplets]
    


        
def find_pair(nums: List[int], start: int, target: int) -> List[int]:
    
    pairs = []
    left, right = start, len(nums)-1
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -=1
        elif sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            # to avoid duplicates
            while left < right and nums[left] == nums[right]:
                left +=1
                
    return pairs

def triplet_sum(nums: List[int]) -> List[List[int]]:
    
    triplets = []
    nums.sort()
    
    for i in range(len(nums)):
        
        # b + c = -a, if b & c is positive it cannt be -a
        if (nums[i] > 0):
            break
        # avoid duplicate, skip if same as previous number (a)
        if i > 0 and nums[i] == nums [i-1]:
            continue
        
        # find two numbers(b,c) that sum to -a in [a,b,c]
        pairs = find_pair(nums, i+1, -nums[i])
        for pair in pairs:
            triplets.append([nums[i]] + pair)
            
    return triplets 
                


nums = list(map(int, input("Type integers with space for list: ").split()))

#print(brute_force(nums))
print(triplet_sum(nums))