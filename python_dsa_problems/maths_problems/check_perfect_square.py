#Maths questions 11-25
#Name: Premnath Sonkusare

def is_perfect_square(num:int)->bool:
    if num<1:
        raise ValueError("Number must be Positive!")
    root = num**0.5
    if root*root == num:
        return True
    return False
if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        is_perf_sq = is_perfect_square(input_num)
        print(f"Input number is Perfect Square:{is_perf_sq}")
    except Exception as e:
            print(type(e).__name__)
            print(str(e))