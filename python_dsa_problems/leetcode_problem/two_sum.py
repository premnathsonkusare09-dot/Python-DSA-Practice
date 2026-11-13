def twoSum(nums: list[int], target: int) -> list[int]:
    list_dict = {}
    for index in range(len(nums)):
        complement = target - nums[index]
        if complement in list_dict:
            return [list_dict[complement], index]
        list_dict[nums[index]] = index
    return []
    

def get_formatted_list(nums: list) -> list:
    formatted_list = []
    for num in nums:
        formatted_list.append(int(num.strip()))
    return formatted_list
    
if __name__ == "__main__":
    try:
        input_string = input("Enter the list (comma-separated): ")
        input_list = input_string.split(",")
        form_list = get_formatted_list(input_list)
        print("Formatted List:", form_list)
        
        inp_target_sum = int(input("Enter the target Sum: "))
        target_sum_index = twoSum(form_list, inp_target_sum)
        print(f"Target Sum present at index: {target_sum_index}")
    except Exception as e:
        print(type(e).__name__)
        print(str(e))