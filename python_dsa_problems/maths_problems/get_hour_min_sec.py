#Maths questions 11-25
#Name: Premnath Sonkusare

def sec_to_hour_min_sec(sec:int)->tuple[int,int,int]:
    hour = sec//3600
    remaining_sec = sec%3600
    min = remaining_sec//60
    seconds = remaining_sec%60
    return hour,min,seconds

if __name__ == "__main__":
    try:
        
        input_sec = int(input("Enter the seconds:"))
        hour,min,sec = sec_to_hour_min_sec(input_sec)
        print(f"Hour:{hour},Minutes:{min},Seconds:{sec}")
    
    except Exception as e:
        print(type(e).__name__)
        print(str(e))
