#Mixed Problems 25-50
#Name: Premnath Sonkusare

def get_fibonacci_series(count:int)->list:
    if count < 0:
        raise ValueError("count must not be negative")
    numbers: list[int] = []
    current = 0
    next_number = 1
    for _ in range(count):
        numbers.append(current)
        current, next_number = next_number, current + next_number
    return numbers

if __name__ == "__main__":
    try:
        input_num = int(input("Enter how many number of fibonacci series you want:"))
        fib_series = get_fibonacci_series(input_num)
        print(f"{input_num} sequence of fibonnaci series is: {fib_series}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))