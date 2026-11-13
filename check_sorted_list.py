#Mixed Problems 25-50
#Name: Premnath Sonkusare

def check_sorted_list(numbers: list[int]) -> bool:
    for index in range(1, len(numbers)):
        if numbers[index] < numbers[index - 1]:
            return False
    return True

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list

if __name__ == "__main__":
    try:
        input_list = list(input("Enter the numbers of list:").split(","))
        form_list = get_formatted_list(input_list)
        is_sorted = check_sorted_list(form_list)
        print(f"Given list is sorted: {is_sorted}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))