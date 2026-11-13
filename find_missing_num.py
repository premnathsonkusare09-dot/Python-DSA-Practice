#Set Problems 51-60
#Name: Premnath Sonkusare

def get_formatted_set(nums:list)->set:
    formatted_set = set()
    for num in nums:
        formatted_set.add(int(num))
    return formatted_set

def find_missing_num_of_set(nums:set[int], start:int, end:int)->set[int]:
    full_set = set(range(start, end + 1))
    return full_set - nums


if __name__=="__main__":
    try:
        set_1 = set(input("Enter the first set:").split(","))
        formatted_set_1 = get_formatted_set(set_1)  
        start = int(input("Enter a start value:"))
        end = int(input("Enter the end value:"))
        missing_values = find_missing_num_of_set(formatted_set_1,start,end)
        print(f"Missing Values of the set is:{missing_values}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))

    




