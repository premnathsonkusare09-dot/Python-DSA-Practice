#Mixed Problems 25-50
#Name: Premnath Sonkusare

def search_by_binary_search(numbers: list[int], target: int) -> tuple[int,bool]:
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle,True
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1,False

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list


if __name__ == "__main__":
    try:
        input_list = list(input("Enter the numbers of list:").split(","))
        form_list = sorted(get_formatted_list(input_list))
        print(f"sorted list is:{form_list}")
        inp_target = int(input("Enter the target valau:"))
        index,is_present = search_by_binary_search(form_list,inp_target)
        print(f"Target Value {inp_target} present at {index+1}th position in a input list:{is_present}")
    except Exception as e:
            print(type(e).__name__)
            print(str(e))