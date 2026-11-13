#Mixed Problems 25-50
#Name: Premnath Sonkusare

def sorting_using_selection_sort(numbers: list[int]) -> list[int]:
    result = numbers.copy()
    for index in range(len(result)):
        smallest_index = index
        for candidate in range(index + 1, len(result)):
            if result[candidate] < result[smallest_index]:
                smallest_index = candidate
        temporary = result[index]
        result[index] = result[smallest_index]
        result[smallest_index] = temporary
    return result

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list

if __name__ == "__main__":
    try:
        input_list = list(input("Enter the numbers of list:").split(","))
        form_list = get_formatted_list(input_list)
        sorted_list = sorting_using_selection_sort(form_list)
        print(f"Sorted List is: {sorted_list}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))