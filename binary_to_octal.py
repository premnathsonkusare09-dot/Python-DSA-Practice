#Maths questions 11-25
#Name: Premnath Sonkusare

def bin_to_oct(num:str)->str:
    if len(num) == 0:
        raise ValueError("Binary number cant be empty!") 
    dec_num = 0
    for digit in num:
        if digit not in "01":
            raise ValueError("Binary number can only contain 0 and 1!")  
        dec_num = dec_num*2+int(digit)
    if dec_num==0:
        return "0"
    oct_num = []
    while dec_num>0:
        oct_num.append(str(dec_num%8))
        dec_num //= 8
    return "".join(reversed(oct_num))

if __name__ == "__main__":
    try:
        input_num = str(input("Enter the binary number:"))
        ans = bin_to_oct(input_num)
        print(f"Octal number of {input_num} is: {ans}")
    except Exception as e:
            print(type(e).__name__)
            print(str(e))