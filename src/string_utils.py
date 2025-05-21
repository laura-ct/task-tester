def reverse_string(input_string: str) -> str:
    """
    Reverse the given string using a manual character-by-character approach.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Use list to manually reverse the string
    reversed_chars = []
    for i in range(len(input_string) - 1, -1, -1):
        reversed_chars.append(input_string[i])
    
    # Convert list back to string
    return ''.join(reversed_chars)