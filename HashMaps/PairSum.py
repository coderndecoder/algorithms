# Find pairs in a sorted list that sums to given number. 
# Return the indexes of the pair. 
# If not found return an empty list

from typing import List

#nums, target = [0, 5 ,6, 9], 11

def pair_sum_unsorted_single_pass(nums: List[int], target: int)->List[int]:
    
    num_map={}
    result = []
    
    for i, x in enumerate(nums):
        num = target - x
        if num in num_map:
            result.append([num_map[num], i])
        num_map[x] = i
        
    return result       
    


nums = list(map(int, input("Type numbers with space for list: ").split()))

target = int(input("Type target sum number: "))
print(pair_sum_unsorted_single_pass(nums, target))