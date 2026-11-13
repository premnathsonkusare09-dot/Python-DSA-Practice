#Maths questions 11-25
#Name: Premnath Sonkusare

def dec_to_hex(num:int)->str:
    if num<0:
        raise ValueError("Number cant be negative!")
    if num==0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    hex_value = []
    while num>0:
        hex_value.append(hex_digits[num%16])
        num //= 16
    return "".join(reversed(hex_value))

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        hex_val = dec_to_hex(input_num)
        print(f"Hexadecimal value of {input_num} is: {hex_val}")
    except Exception as e:
            print(type(e).__name__)
            print(str(e))