 #1.1 Implement a recursive function to calculate the factorial of a given number.

def factorial(n):
 
    if n < 1:
        return 1
 # use the recurrence relation
    return n * factorial(n - 1)
 
 
if __name__ == '__main__':
 
    n = 5
    print(f'The Factorial of {n} is', factorial(n))