#Mixed Problems 25-50
#Name: Premnath Sonkusare

def get_mult_table(num:int)->list[int]:
    table = list()
    for i in range(1, 11):
        table.append(num * i)
    return table

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        mult_table = get_mult_table(input_num)
        print(f"Multiplication Table of {input_num} is: {mult_table}")  
    except Exception as e:
        print(type(e).__name__)
        print(str(e))
       