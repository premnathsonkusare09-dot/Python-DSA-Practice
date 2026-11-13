#Mixed Problems 25-50
#Name: Premnath Sonkusare

def find_num_sign(num:int)->str:
    if num<0:
        return "Negative"
    if num>0:
        return "Positive"
    return "Zero"

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        check_sign = find_num_sign(input_num)
        print(f"Sign of the Given number {input_num} is : {check_sign}")
    except Exception as e:
            print(type(e).__name__)
            print(str(e))
        