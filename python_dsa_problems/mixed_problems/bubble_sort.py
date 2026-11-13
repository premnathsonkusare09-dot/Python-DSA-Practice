#Mixed Problems 25-50
#Name: Premnath Sonkusare

def sorting_using_bubble_sort(numbers: list[int]) -> list[int]:
    result = numbers.copy()
    for end in range(len(result) - 1, 0, -1):
        for index in range(end):
            if result[index] > result[index + 1]:
                temporary = result[index]
                result[index] = result[index + 1]
                result[index + 1] = temporary
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
        sorted_list = sorting_using_bubble_sort(form_list)
        print(f"Sorted List is: {sorted_list}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))