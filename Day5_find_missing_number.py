def find_missing_number_sum(numbers):
    """
    Find the missing number using sum formula approach.
    
    Args:
        numbers (list): List of integers from 1 to n with one number missing
    
    Returns:
        int: The missing number
    
    Example:
        >>> find_missing_number_sum([1, 2, 4, 5, 6])
        3
    """
    if not numbers:
        return 1
    
    n = len(numbers) + 1  # Total numbers should be n
    expected_sum = n * (n + 1) // 2  # Sum formula: 1+2+...+n = n(n+1)/2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


def find_missing_number_set(numbers):
    """
    Find the missing number using set difference approach.
    
    Args:
        numbers (list): List of integers from 1 to n with one number missing
    
    Returns:
        int: The missing number
    """
    if not numbers:
        return 1
    
    n = len(numbers) + 1
    expected_set = set(range(1, n + 1))
    actual_set = set(numbers)
    missing = expected_set - actual_set
    return missing.pop()  # Get the single missing element


def find_missing_number_xor(numbers):
    """
    Find the missing number using XOR approach (most efficient).
    
    XOR properties used:
    - a ^ a = 0 (any number XORed with itself is 0)
    - a ^ 0 = a (any number XORed with 0 is itself)
    - XOR is commutative and associative
    
    Args:
        numbers (list): List of integers from 1 to n with one number missing
    
    Returns:
        int: The missing number
    """
    if not numbers:
        return 1
    
    n = len(numbers) + 1
    xor_all = 0
    xor_present = 0
    
    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i
    
    # XOR all present numbers
    for num in numbers:
        xor_present ^= num
    
    # Missing number = XOR of all numbers ^ XOR of present numbers
    return xor_all ^ xor_present


def find_missing_number_binary_search(numbers):
    """
    Find the missing number using binary search (for sorted arrays).
    
    Args:
        numbers (list): Sorted list of integers from 1 to n with one number missing
    
    Returns:
        int: The missing number
    """
    if not numbers:
        return 1
    
    sorted_numbers = sorted(numbers)  # Ensure the list is sorted without modifying the input
    left, right = 0, len(sorted_numbers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If sorted_numbers[mid] == mid + 1, missing number is on the right
        if sorted_numbers[mid] == mid + 1:
            left = mid + 1
        else:
            # Missing number is on the left (or is mid + 1)
            right = mid - 1
    
    return left + 1


# Performance testing function
import time
import random

def performance_test(size=1000000):
    """
    Test performance of different approaches with large datasets.
    """
    # Create a large list with one missing number
    complete_list = list(range(1, size + 1))
    missing_num = random.randint(1, size)
    test_list = [x for x in complete_list if x != missing_num]
    
    print(f"Testing with {size} numbers, missing number: {missing_num}")
    
    methods = [
        ("Sum Formula", find_missing_number_sum),
        ("Set Difference", find_missing_number_set),
        ("XOR Method", find_missing_number_xor),
        ("Binary Search", find_missing_number_binary_search)
    ]
    
    for name, method in methods:
        start_time = time.time()
        result = method(test_list)
        end_time = time.time()
        
        print(f"{name}: {result} (Time: {end_time - start_time:.6f}s)")
        assert result == missing_num, f"{name} failed!"


# Test the functions
if __name__ == "__main__":
    print("=== Find Missing Number ===\n")
    
    # Test cases
    test_cases = [
        [1, 2, 4, 5, 6],  # Missing 3
        [2, 3, 4, 5, 6],  # Missing 1
        [1, 2, 3, 4, 5],  # Missing 6 (last number)
        [1, 3, 4, 5, 6, 7, 8, 9, 10],  # Missing 2
        [2],  # Only one number, missing 1
        []  # Empty list, missing 1
    ]
    
    for i, test_list in enumerate(test_cases, 1):
        print(f"Test Case {i}: {test_list}")
        
        # Test all methods
        result_sum = find_missing_number_sum(test_list)
        result_set = find_missing_number_set(test_list)
        result_xor = find_missing_number_xor(test_list)
        result_binary = find_missing_number_binary_search(test_list)
        
        print(f"  Sum Formula: {result_sum}")
        print(f"  Set Difference: {result_set}")
        print(f"  XOR Method: {result_xor}")
        print(f"  Binary Search: {result_binary}")
        
        # Verify all methods give same result
        all_same = result_sum == result_set == result_xor == result_binary
        print(f"  All methods agree: {all_same}")
        print()
    
    # Explain the mathematical approach
    print("=== Mathematical Explanation ===")
    print("Sum Formula Approach:")
    print("- Expected sum of 1 to n: n(n+1)/2")
    print("- For [1,2,4,5,6]: n=6, expected_sum=21, actual_sum=18")
    print("- Missing number = 21 - 18 = 3")
    print()
    
    print("XOR Approach:")
    print("- XOR all numbers 1 to n: 1^2^3^4^5^6")
    print("- XOR all present numbers: 1^2^4^5^6")
    print("- Result: (1^2^3^4^5^6) ^ (1^2^4^5^6) = 3")
    print("- Because a^a=0, only the missing number remains")
    print()
    
    # Performance comparison
    print("=== Performance Comparison ===")
    try:
        performance_test(100000)  # Test with 100k numbers
    except Exception as e:
        print(f"Performance test skipped: {e}")
    
    print("\n=== Time Complexity Analysis ===")
    print("Sum Formula: O(n) time, O(1) space")
    print("Set Difference: O(n) time, O(n) space")
    print("XOR Method: O(n) time, O(1) space - Most efficient!")
    print("Binary Search: O(n log n) time, O(1) space (due to sorting)")