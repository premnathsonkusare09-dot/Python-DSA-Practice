#Mixed Problems 25-50
#Name: Premnath Sonkusare

def find_lcm(first,second)->int:
    if first <= 0 or second <= 0:
        raise ValueError("numbers must be positive")
    left = first
    right = second
    while right != 0:
        left, right = right, left % right
    gcd = left
    return first * second // gcd

if __name__ == "__main__":
    try:
        input_num1 = int(input("Enter the first number:"))
        input_num2 = int(input("Enter the second number:"))
        lcm = find_lcm(input_num1,input_num2)
        print(f"LCM of {input_num1} and {input_num2} is: {lcm}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))