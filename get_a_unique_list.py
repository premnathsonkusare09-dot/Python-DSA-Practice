#Set Problems 51-60
#Name: Premnath Sonkusare

def get_formatted_list(nums:list)->list:
    formatted_list = list()
    for num in nums:
        formatted_list.append(int(num))
    return formatted_list

def get_unique_list_by_set(nums:list)->set:
   return set(nums)

if __name__=="__main__":
    try:
        input_list = list(input("Enter the list:").split(","))
        inp_list = get_formatted_list(input_list)
        unique_list = get_unique_list_by_set(inp_list)
        print(f"Unique List is:{unique_list}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))