#Set Problems 51-60
#Name: Premnath Sonkusare

def find_set_intersection(left:set[int],right:set[int])->set[int]:
    return left & right

def get_formatted_set(nums:list)->set:
    formatted_set = set()
    for num in nums:
        formatted_set.add(int(num))
    return formatted_set

if __name__=="__main__":
    try:    
        set_1 = set(input("Enter the first set:").split(","))
        set_2 = set(input("Enter the second set:").split(","))
        formatted_set_1 = get_formatted_set(set_1)  
        formatted_set_2 = get_formatted_set(set_2)  
        set_intersection = find_set_intersection(formatted_set_1, formatted_set_2)
        print(f"Intersection of set {formatted_set_1} and {formatted_set_2} is: {set_intersection}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))
