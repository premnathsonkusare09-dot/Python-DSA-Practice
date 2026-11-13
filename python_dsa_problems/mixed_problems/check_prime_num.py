#Mixed Problems 25-50
#Name: Premnath Sonkusare

def check_prime_num(num:int)->bool:
    if num<2:
        return False
    factor = 2
    while factor<num:
        if num%factor == 0:
            return False
        factor += 1
    return True

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        is_prime = check_prime_num(input_num)
        print(f"Given number {input_num} is prime number: {is_prime}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))