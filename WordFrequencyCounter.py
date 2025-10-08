// Word Frequency Counter
def word_frequency(text):
    """
    Count the frequency of each word in the given text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    # Normalize the text to lowercase and split into words
    words = text.lower().split()
    # Use a dictionary to count the frequency of each word
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


# Test the function
if __name__ == "__main__":
    test_text = "Hello world! Hello everyone."
    print(f"Input: '{test_text}'")
    print(f"Output: {word_frequency(test_text)}")

    # Additional test cases
    test_cases = [
        "Python is great",
        "Hello Hello world",
        "Test test TEST",
        "123 123 456",
        ""
    ]

    print("\nAdditional test cases:")
    for i, test in enumerate(test_cases, 1):
        result = word_frequency(test)
        print(f"Test {i}: '{test}' -> {result}")