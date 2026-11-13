#Set Problems 51-60
#Name: Premnath Sonkusare

def remove_value_from_set(nums:set[int], value:int)->set[int]:
    result = nums.copy()
    result.discard(value)
    return result

def get_formatted_set(nums:list)->set:
    formatted_set = set()
    for num in nums:
        formatted_set.add(int(num))
    return formatted_set

if __name__=="__main__":
    try:
        set_1 = set(input("Enter the first set:").split(","))
        value = int(input("Enter the value to remove from a set (only one):"))
        formatted_set_1 = get_formatted_set(set_1)  
        removed_value_set = remove_value_from_set(formatted_set_1,value)
        print(f"Set after removing a value is: {removed_value_set}")   
    except Exception as e:
        print(type(e).__name__)
        print(str(e))