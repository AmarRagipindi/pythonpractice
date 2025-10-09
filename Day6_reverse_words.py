def reverse_words(sentence):
    """
    Reverse the order of words in a sentence.
    
    Args:
        sentence (str): The input sentence to reverse words
    
    Returns:
        str: Sentence with words in reversed order
    
    Example:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("Python is awesome")
        'awesome is Python'
    """
    # Split the sentence into words, reverse the list, and join them back
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


# Alternative solution using reversed() function
def reverse_words_reversed(sentence):
    """
    Alternative implementation using the reversed() function.
    """
    words = sentence.split()
    return ' '.join(reversed(words))


# Alternative solution using a loop
def reverse_words_loop(sentence):
    """
    Alternative implementation using a traditional loop.
    """
    words = sentence.split()
    reversed_list = []
    for i in range(len(words) - 1, -1, -1):
        reversed_list.append(words[i])
    return ' '.join(reversed_list)


# Alternative solution preserving multiple spaces
def reverse_words_preserve_spaces(sentence):
    """
    Alternative implementation that preserves multiple spaces between words.
    This splits on any whitespace but keeps the original spacing pattern.
    """
    import re
    # Split on whitespace while keeping the delimiters
    words = [word for word in sentence.split() if word]
    return ' '.join(reversed(words))


# Test the function
if __name__ == "__main__":
    # Basic test cases
    test_sentence = "Hello World"
    print(f"Input: '{test_sentence}'")
    print(f"Output (slice method): {reverse_words(test_sentence)}")
    print(f"Output (reversed function): {reverse_words_reversed(test_sentence)}")
    print(f"Output (loop method): {reverse_words_loop(test_sentence)}")
    print()
    
    # Additional test cases
    test_cases = [
        "Python is awesome",
        "Hello World!",
        "I love programming",
        "a b c d e",
        "One",
        "",
        "  spaces  before  and  after  ",
        "The quick brown fox jumps over the lazy dog"
    ]
    
    print("Additional test cases:")
    for i, test in enumerate(test_cases, 1):
        result = reverse_words(test)
        print(f"Test {i}: '{test}' -> '{result}'")
    
    # Demonstrate that different methods produce same results
    print(f"\nVerifying all methods produce same result for 'Hello World':")
    methods = [reverse_words, reverse_words_reversed, reverse_words_loop]
    results = [method("Hello World") for method in methods]
    all_same = all(result == results[0] for result in results)
    print(f"All methods produce same result: {all_same}")
    
    # Show step-by-step for understanding
    print("\n=== Step-by-step explanation ===")
    example = "Python is awesome"
    print(f"Original sentence: '{example}'")
    words_list = example.split()
    print(f"After split(): {words_list}")
    reversed_list = words_list[::-1]
    print(f"After reverse: {reversed_list}")
    result = ' '.join(reversed_list)
    print(f"After join(): '{result}'")
