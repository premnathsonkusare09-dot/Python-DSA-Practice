#Mixed Problems 25-50
#Name: Premnath Sonkusare

def check_leap_year(year:int)->bool:
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    return year%4 == 0

if __name__ == "__main__":
    try:
        input_year = int(input("Enter a year:"))
        is_leap_year = check_leap_year(input_year)
        print(f"{input_year} is Leap year : {is_leap_year}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))
