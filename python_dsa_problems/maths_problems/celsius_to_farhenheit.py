#Maths questions 11-25
#Name: Premnath Sonkusare

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    try:
        input_temp = int(input("Enter the temperature in celsius:"))
        fah_temp = celsius_to_fahrenheit(input_temp)
        print(f"Given temperature in fahrenheit is: {fah_temp}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))
