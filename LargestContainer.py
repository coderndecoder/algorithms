# Array of numbers representing height of line on graph along x-axis, 
# return amount of water with largest container formed from two lines.

# height = [2 7 8 3 7 6] output = 24 
from typing import List

def brute_force(heights: List[int]) -> int:
    
    n = len(heights)
    max_amt = 0
    
    for i in range(n):
        for j in range(i+1, n):
            amt = min(heights[i], heights[j]) * (j-i)
            max_amt = max(max_amt, amt)
            
    return max_amt

def single_pass(heights: List[int]) -> int:
    
    n = len(heights)
    max_amt = 0
    left, right = 0, n-1
    
    while left < right:
        amt = min(heights[left], heights[right]) * (right-left)
        max_amt = max(max_amt, amt)
        
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        elif heights[left] == heights[right]:
            left += 1
            right -= 1
        
    return max_amt
    

heights = list(map(int,input("Enter numbers with space:").split()))

#print(brute_force(heights))
print(single_pass(heights))
