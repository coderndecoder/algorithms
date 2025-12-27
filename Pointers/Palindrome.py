# Check if String is a palindrome, remove non-alpha-numberic.

# racecar <=> racecar

 
def check_palindrome(s: str) -> bool:
    
    left, right = 0, len(s)-1
    
    while left < right:
        
        while left < right and not s[left].isalnum:
            left += 1
        while left < right and not s[right].isalnum:
            right -= 1
            
        if s[left] != s[right]:
            return False
        
        left +=1
        right -=1
    return True
    
    

word = input("Input String to check for Palindrome: ") 

print(check_palindrome(word))

