#list questions 1-10 
#Name: Premnath Sonkusare

#find largest number in a list
def find_largest_number(nums:list)->int:
  largest = float("-inf")
  for num in nums:
    if num>largest:
      largest = num
  return largest

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list

if __name__ == "__main__":

#for largest number of list
    input_list = list(input("Enter the numbers of a list").split(","))
    formatted_list = get_formatted_list(input_list)
    print(f"Given list is: {formatted_list}")
    largest_num = find_largest_number(formatted_list)
    print(f"largest number of a list is:{largest_num}")
