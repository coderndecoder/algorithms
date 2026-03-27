# Determine if number is Happy Number. Output : True
# Ex - 23 = 2^2 + 3^2 = 13 = 1^2 + 3^2 = 10 = 1^2 + 0^2 = 1

from LinkedList import LinkedList

class HappyNumber:
    def find_if_happy_number(num :int) -> bool:
        slow = fast = num
        
        while True:
            slow = HappyNumber.get_next_number(slow)
            fast = HappyNumber.get_next_number(HappyNumber.get_next_number(fast))
            
            if fast == 1:
                return True
            elif slow == fast:
                return False
        
    # Calculate next number    
    def get_next_number(n : int) -> int:
        next_num = 0
        while n > 0:
            num = n%10
            next_num += num**2
            n //= 10
        
        return next_num
        
        
if __name__ == "__main__":
    
    n = 23
    result = HappyNumber.find_if_happy_number(n)
    print(f"{n} is Happy Number: {result}")
    n=116
    result = HappyNumber.find_if_happy_number(n)
    print(f"{n} is Happy Number: {result}")
        