def even_numbers_squared(numbers):
    """
    Takes a list of numbers and returns a new list containing only the even numbers, but squared.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        list: A list of squared even numbers
    
    Example:
        >>> even_numbers_squared([1, 2, 3, 4, 5, 6])
        [4, 16, 36]
    """
    # Using list comprehension to filter even numbers and square them
    return [num ** 2 for num in numbers if num % 2 == 0]


# Alternative solution using traditional loop
def even_numbers_squared_loop(numbers):
    """
    Alternative implementation using a traditional for loop.
    """
    result = []
    for num in numbers:
        if num % 2 == 0:  # Check if number is even
            result.append(num ** 2)  # Square the even number
    return result


# Test the function
if __name__ == "__main__":
    # Test cases
    test_list = [1, 2, 3, 4, 5, 6]
    print(f"Input: {test_list}")
    print(f"Output (list comprehension): {even_numbers_squared(test_list)}")
    print(f"Output (loop method): {even_numbers_squared_loop(test_list)}")
    
    # Additional test cases
    test_cases = [
        [1, 3, 5, 7],  # All odd numbers
        [2, 4, 6, 8],  # All even numbers
        [0, -2, -3, 4, -5, 6],  # Mixed with negative numbers and zero
        []  # Empty list
    ]
    
    print("\nAdditional test cases:")
    for i, test in enumerate(test_cases, 1):
        result = even_numbers_squared(test)
        print(f"Test {i}: {test} -> {result}")