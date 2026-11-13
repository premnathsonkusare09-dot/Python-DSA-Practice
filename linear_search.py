#Mixed Problems 25-50
#Name: Premnath Sonkusare

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list

def search_by_linear_search(numbers: list[int], target: int) -> tuple[int,bool]:
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index,True
    return -1,False

if __name__ == "__main__":
    try:
        input_list = list(input("Enter the numbers of list:").split(","))
        form_list = get_formatted_list(input_list)
        inp_target = int(input("Enter the target valau:"))
        index,is_present = search_by_linear_search(form_list,inp_target)
        print(f"Target Value {inp_target} present at {index+1}th position in a input list:{is_present}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))