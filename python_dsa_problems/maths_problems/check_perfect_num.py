#Maths questions 11-25
#Name: Premnath Sonkusare

def is_perfect_number(number:int)->bool:
    if number < 1:
        raise False
    if number==1:
        return False
    total =1
    factor = 2
    while factor * factor < number:
        if number % factor == 0:
            total += factor
            if factor != number // factor:
                total += number // factor
        factor += 1
    return total == number

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        is_perf_num = is_perfect_number(input_num)
        print(f"Input number is Perfect Number:{is_perf_num}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))
                    