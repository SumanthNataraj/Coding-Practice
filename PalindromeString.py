"""You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards."""

def isPalindrome(self, S):
        # code here
        str=S[::-1]
        
        if(S==str):
            return 1
            
        return 0

# Test the function with a sample string

s = "racecar"
print(isPalindrome(s))  # Output: 1
