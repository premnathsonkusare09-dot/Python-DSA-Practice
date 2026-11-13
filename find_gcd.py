#Mixed Problems 25-50
#Name: Premnath Sonkusare

def find_gcd(first: int, second: int) -> int:
    if first <= 0 or second <= 0:
        raise ValueError("numbers must be positive")
    while second != 0:
        remainder = first % second
        first = second
        second = remainder
    return first

if __name__ == "__main__":
    try:
        input_num1 = int(input("Enter the first number:"))
        input_num2 = int(input("Enter the second number:"))
        gcd = find_gcd(input_num1,input_num2)
        print(f"GCD of {input_num1} and {input_num2} is: {gcd}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))