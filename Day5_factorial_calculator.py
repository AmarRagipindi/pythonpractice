def factorial_iterative(n):
    """
    Calculate factorial using iterative approach.
    
    Args:
        n (int): Non-negative integer to calculate factorial for
    
    Returns:
        int: Factorial of n
    
    Example:
        >>> factorial_iterative(5)
        120
        >>> factorial_iterative(0)
        1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    """
    Calculate factorial using recursive approach.
    
    Args:
        n (int): Non-negative integer to calculate factorial for
    
    Returns:
        int: Factorial of n
    
    Example:
        >>> factorial_recursive(5)
        120
        >>> factorial_recursive(0)
        1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base case: 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


# Alternative using math module
import math

def factorial_math(n):
    """
    Calculate factorial using built-in math.factorial() function.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)


# Performance comparison function
import time

def compare_performance(n):
    """
    Compare performance of different factorial implementations.
    """
    print(f"Calculating factorial of {n}:")
    
    # Iterative approach
    start_time = time.time()
    result_iter = factorial_iterative(n)
    iter_time = time.time() - start_time
    
    # Recursive approach
    start_time = time.time()
    result_rec = factorial_recursive(n)
    rec_time = time.time() - start_time
    
    # Math module approach
    start_time = time.time()
    result_math = factorial_math(n)
    math_time = time.time() - start_time
    
    print(f"Iterative: {result_iter} (Time: {iter_time:.6f}s)")
    print(f"Recursive: {result_rec} (Time: {rec_time:.6f}s)")
    print(f"Math module: {result_math} (Time: {math_time:.6f}s)")
    print(f"All results match: {result_iter == result_rec == result_math}")
    print()


# Test the functions
if __name__ == "__main__":
    # Basic test cases
    test_cases = [0, 1, 5, 10]
    
    print("=== Factorial Calculator ===\n")
    
    for n in test_cases:
        print(f"Factorial of {n}:")
        print(f"  Iterative: {factorial_iterative(n)}")
        print(f"  Recursive: {factorial_recursive(n)}")
        print(f"  Math module: {factorial_math(n)}")
        print()
    
    # Show step-by-step calculation for better understanding
    print("=== Step-by-step calculation for 5! ===")
    print("5! = 5 × 4 × 3 × 2 × 1")
    print("   = 5 × 4!")
    print("   = 5 × 24")
    print("   = 120")
    print()
    
    # Performance comparison for larger numbers
    print("=== Performance Comparison ===")
    for n in [10, 15, 20]:
        compare_performance(n)
    
    # Error handling demonstration
    print("=== Error Handling ===")
    try:
        factorial_iterative(-5)
    except ValueError as e:
        print(f"Error with negative number: {e}")
    
    # Fun facts about factorials
    print("\n=== Fun Facts ===")
    print("0! = 1 (by mathematical convention)")
    print("1! = 1")
    print("10! = 3,628,800")
    print("20! = 2,432,902,008,176,640,000")
    print("Factorials grow very quickly!")
    
    # Show first 10 factorials
    print("\nFirst 10 factorials:")
    for i in range(10):
        print(f"{i}! = {factorial_iterative(i)}")