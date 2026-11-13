#Mixed Problems 25-50
#Name: Premnath Sonkusare

def find_sum_of_digits(number:int)->int:
    if number < 0:
        raise ValueError("number must not be negative")
    total = 0
    while number > 0:
        total = total + number % 10
        number = number // 10
    return total

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        sum_of_digits = find_sum_of_digits(input_num)       
        print(f"Sum of digits of {input_num} is: {sum_of_digits}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))