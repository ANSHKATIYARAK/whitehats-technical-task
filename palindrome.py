"""
WhiteHats Recruitment Task - Technical Domain
Question 3: Palindrome verification function
"""

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome.
    Ignores casing, whitespace, and non-alphanumeric characters.
    """
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_cases = [
        ("racecar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
    ]

    for text, expected in test_cases:
        result = is_palindrome(text)
        print(f"'{text}' -> {result} (Expected: {expected})")
        assert result == expected
    print("\nAll palindrome test cases passed successfully!")
