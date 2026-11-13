#Maths questions 11-25
#Name: Premnath Sonkusare

def bin_to_dec(num:str)->int:
    if len(num) == 0:
       raise ValueError("Binary number cant be empty!") 
    dec_num = 0
    for digit in num:
       if digit not in "01":
           raise ValueError("Binary number can only contain 0 and 1!")  
       dec_num = dec_num*2+int(digit)
    return dec_num

if __name__ == "__main__":
    try:
        input_num = str(input("Enter the binary number:"))
        dec_num = bin_to_dec(input_num)
        print(f"Decimal number of {input_num} is:{dec_num}")
    except Exception as e:
            print(type(e).__name__)
            print(str(e))