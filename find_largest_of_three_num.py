#Mixed Problems 25-50
#Name: Premnath Sonkusare

def largest_of_three(first: int, second: int, third: int) -> int:
    largest = first
    if second > largest:
        largest = second
    if third > largest:
        largest = third
    return largest

if __name__ == "__main__":
    try:
        input_num1 = int(input("Enter the first number:"))
        input_num2 = int(input("Enter the second number:"))
        input_num3 = int(input("Enter the third number:"))
        check_largest = largest_of_three(input_num1, input_num2, input_num3)
        print(f"Largest of three number is:{check_largest}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))