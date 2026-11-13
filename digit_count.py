#Mixed Problems 25-50
#Name: Premnath Sonkusare

def count_digits(num:int)->int:
    return len(str(num))

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        digit_count = count_digits(input_num)
        print(f"Digits count of {input_num} is: {digit_count}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))