#Maths questions 11-25
#Name: Premnath Sonkusare

def count_num_of_divisors(number:int)->int:
    if number < 1:
        raise ValueError("number must be positive")
    count = 0
    factor = 1
    while factor * factor <= number:
        if number % factor == 0:
            count += 1
            if factor != number // factor:
                count += 1
        factor += 1
    return count

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        counts = count_num_of_divisors(input_num)
        print(f"Count of divisors are : {counts}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))