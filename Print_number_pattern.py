"""You are given a number n. You need to generate and print a pattern based on the given value of n.

For each row, starting from the first, print numbers in descending order from n down to 1.
Each number in a row is repeated as many times as the current row index (starting from n).
Instead of printing each row on a new line, separate rows with -1.
Instead of a newline at the end of each row, print -1 to indicate row separation. After printing the entire pattern, end the output with -1.

For n= 3,
pattern:  3 3 3 2 2 2 1 1 1
          3 3 2 2 1 1 
          3 2 1

For n= 2,
pattern:  2 2 1 1
          2 1
"""

def print_pattern(n):
    result=[]
    for i in range(n):
        for j in range(n,0,-1):
            for k in range(n-i):
                result.append(j)
        result.append(-1)
    return result
        
# Test the function with given examples

for i in range(1,5):
    print(print_pattern(i))
    print("--------------------------------")