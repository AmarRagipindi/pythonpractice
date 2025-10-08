def character_count(text):
    """
    Takes a string and returns a dictionary where the keys are the characters 
    in the string and the values are the number of times each character appears.
    
    Args:
        text (str): Input string to analyze
    
    Returns:
        dict: Dictionary with characters as keys and their counts as values
    
    Example:
        >>> character_count("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # Using dictionary comprehension with set to get unique characters
    return {char: text.count(char) for char in set(text)}


# Alternative solution using traditional loop
def character_count_loop(text):
    """
    Alternative implementation using a traditional for loop.
    """
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


# Alternative solution using get() method
def character_count_get(text):
    """
    Alternative implementation using the get() method.
    """
    char_dict = {}
    for char in text:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict


# Alternative solution using collections.Counter
from collections import Counter

def character_count_counter(text):
    """
    Alternative implementation using collections.Counter.
    """
    return dict(Counter(text))


# Test the function
if __name__ == "__main__":
    # Test cases
    test_string = "hello"
    print(f"Input: '{test_string}'")
    print(f"Output (dict comprehension): {character_count(test_string)}")
    print(f"Output (loop method): {character_count_loop(test_string)}")
    print(f"Output (get method): {character_count_get(test_string)}")
    print(f"Output (Counter method): {character_count_counter(test_string)}")
    
    # Additional test cases
    test_cases = [
        "python",
        "aabbcc",
        "Programming",
        "Hello World!",
        "aA",  # Case sensitivity test
        "",   # Empty string
        "   ", # Spaces only
        "123321"  # Numbers
    ]
    
    print("\nAdditional test cases:")
    for i, test in enumerate(test_cases, 1):
        result = character_count(test)
        print(f"Test {i}: '{test}' -> {result}")
    
    # Demonstrate that different methods produce same results
    print(f"\nVerifying all methods produce same result for 'hello':")
    methods = [character_count, character_count_loop, character_count_get, character_count_counter]
    results = [method("hello") for method in methods]
    all_same = all(result == results[0] for result in results)
    print(f"All methods produce same result: {all_same}")