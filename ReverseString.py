"""You are given a string s, and your task is to reverse the string."""
def reverseWord(self, str: str) -> str:
    
        str=str[::-1]
        
        return str

# Test the function with a sample string

print(reverseWord("Hello World!")) # Output: "!dlroW olleH"

print(reverseWord("This is a test.")) # Output: ".tset a si sihT"

print(reverseWord("Python is fun!")) # Output: "!nuf ytpnoH"