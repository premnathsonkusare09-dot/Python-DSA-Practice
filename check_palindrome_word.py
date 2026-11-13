#Mixed Problems 25-50
#Name: Premnath Sonkusare

def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left = left + 1
        right = right - 1
    return True

if __name__ == "__main__":
    try:
        input_str = str(input("Enter the String:"))
        is_palindrome_str = is_palindrome(input_str)
        print(f"Given String is Palindrome: {is_palindrome_str}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))