#Maths questions 11-25
#Name: Premnath Sonkusare

def find_digital_root(number:int)->int:
    if number < 0:
        raise ValueError("number must be non-negative")
    while number >= 10:
        total = 0
        for character in str(number):
            total += int(character)
        number = total
    return number

if __name__ == "__main__":
    try:
        input_num = int(input("Enter the number:"))    
        find_dig_root = find_digital_root(input_num)
        print(f"Digital root of {input_num} is: {find_dig_root}")   
    except Exception as e:
        print(type(e).__name__)
        print(str(e))