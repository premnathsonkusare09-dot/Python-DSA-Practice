#Maths questions 11-25
#Name: Premnath Sonkusare

def decimal_to_base(number: int, base: int) -> str:
    if number < 0:
        raise ValueError("number must be non-negative")
    if base < 2 or base > 16:
        raise ValueError("base must be from 2 to 16")
    if number == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result: list[str] = []
    while number > 0:
        result.append(digits[number % base])
        number //= base
    return "".join(reversed(result))

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the Decimal number:"))
        input_base = int(input("Enter the base of the number(2,8,10,16) which you want to convert:"))
        any_base = decimal_to_base(input_num,input_base)
        print(f"Decimal number in base{input_base} is :{any_base}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))