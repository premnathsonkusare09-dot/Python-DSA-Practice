#Maths questions 11-25
#Name: Premnath Sonkusare

def dec_to_bin(num:int)->str:
    if num<0:
        raise ValueError("Number cant be negative!")
    if num==0:
        return "0"
    bin_num = []
    while num>0:
        bin_num.append(str(num%2))
        num //= 2
    return "".join(reversed(bin_num))

if __name__ == "__main__":
    try:   
        input_num = int(input("Enter the number:"))
        bin_num = dec_to_bin(input_num)
        print(f"Binary number of {input_num} is:{bin_num}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))