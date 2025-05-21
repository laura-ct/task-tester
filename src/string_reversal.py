def reverse_string(input_string: str) -> str:
    """
    Reverse the given input string manually, without using slice notation or built-in reverse methods.

    This implementation provides a robust, type-hinted string reversal method that:
    - Performs type checking
    - Uses an efficient two-pointer swap technique
    - Works with various string types, including Unicode

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters for efficient manipulation
    chars = list(input_string)
    
    # Manually reverse the list of characters using two-pointer technique
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters from both ends
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert list back to string and return
    return ''.join(chars)