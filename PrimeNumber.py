"""Given a number n, determine whether it is a prime number or not. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself."""
def isPrime(self, n):
    
        # If n is less than or equal to 1, it is not prime
        if n <= 1:
            return False
        
        # Check divisibility for numbers from 2 to the square root of n
        for i in range(2, int(n**0.5) + 1):
            # If n is divisible by any number, it is not prime
            
            if n % i == 0:
                return False

        return True

# Test the function with an example

n = 17
print(isPrime(n))  # Output: True

n = 18
print(isPrime(n))  # Output: False