"""You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards."""

def isPalindrome(S):
        # code here
        str=S[::-1]
        
        if(S==str):
            return True
            
        return False

# Test the function with a sample string

s = "racecar"
print(isPalindrome(s))  # Output: True

s = "hello"

print(isPalindrome(s))  # Output: False
