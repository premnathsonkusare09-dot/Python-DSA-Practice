#Mixed Problems 25-50
#Name: Premnath Sonkusare

def get_fizzbuzz_sequence(num:int)->list:
    if num<0:
        raise ValueError("Number not be Negetive!")
    result = list()
    for n in range(1,num+1):
        if n % 15 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(n))
    return result

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number for Fizzzbuzz series:"))
        fiz_seq = get_fizzbuzz_sequence(input_num)
        print(f"{input_num} number of Fizzbuzz sequence is: {fiz_seq}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))
    