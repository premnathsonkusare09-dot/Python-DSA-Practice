#Maths questions 11-25
#Name: Premnath Sonkusare

def find_sum_upto_n(num:int)->int:
    if num< 1:
        raise ValueError("Number must be positive!")
    total_sum = 0
    for n in range(num+1):
        total_sum += n
    return total_sum

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        total_sum = find_sum_upto_n(input_num)
        print(f"Total Sum is: {total_sum}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))