#Mixed Problems 25-50
#Name: Premnath Sonkusare

def find_factorial(number: int) -> int:
    if number < 0:
        raise ValueError("number must not be negative")
    result = 1
    for value in range(2, number + 1):
        result = result * value
    return result

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        factorial_num = find_factorial(input_num)
        print(f"Factorial of {input_num} is: {factorial_num}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))