#Maths questions 11-25
#Name: Premnath Sonkusare

def find_sum_of_divisors(number:int)->int:
    if number < 1:
            raise ValueError("number must be positive")
    total_sum = 0
    factor = 1
    while factor * factor <= number:
        if number % factor == 0:
            total_sum += factor
            if factor != number // factor:
                total_sum = total_sum+(number//factor)
        factor += 1
    return total_sum

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        total_sum = find_sum_of_divisors(input_num)
        print(f"total sum of divisors is: {total_sum}")
    except Exception as e:
                print(type(e).__name__)
                print(str(e))