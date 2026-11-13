# Maths questions 11-25
# Name: Premnath Sonkusare

def hex_to_dec(num: str) -> int:
    # Convert input to uppercase to handle lowercase hex letters
    num = num.upper()
    
    if len(num) == 0:
        raise ValueError("Hexadecimal number can't be empty!")
        
    dec_num = 0
    hex_digits = "0123456789ABCDEF"
    
    for digit in num:
        # Fix: Check against valid hex_digits, not the input string
        if digit not in hex_digits:
            raise ValueError(f"Character '{digit}' is not a valid hexadecimal number!")
            
        # Convert hex digit to its decimal value (0-15)
        digit_val = hex_digits.index(digit)
        dec_num = dec_num * 16 + digit_val
        
    return dec_num

if __name__ == "__main__":
    try:
        input_num = input("Enter the hexadecimal number: ")
        dec_val = hex_to_dec(input_num)
        print(f"Decimal Value of {input_num} is : {dec_val}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))