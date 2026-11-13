#Mixed Problems 25-50
#Name: Premnath Sonkusare

def get_reverse_num(number:int)->int:
    if number < 0:
       number = abs(number)
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    return reversed_number

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))
        count_zeros = str(input_num).count('0')
        for zero in str(input_num):
            if zero == '0':
                count_zeros += 1
        inp_copy = input_num
        reverse_num = get_reverse_num(inp_copy)
        if count_zeros > 0:
            reverse_num = reverse_num * (10 ** count_zeros)
        if input_num<0:
            reverse_num *= (-1)
        print(f"Reverse of the Given number {input_num} is: {reverse_num}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))