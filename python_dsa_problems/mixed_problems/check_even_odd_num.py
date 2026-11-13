#Mixed Problems 25-50
#Name: Premnath Sonkusare

def check_even_or_odd(num:int)->str:
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        check_num = check_even_or_odd(input_num)
        print(f"Given Number {input_num} is: {check_num} number.")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))