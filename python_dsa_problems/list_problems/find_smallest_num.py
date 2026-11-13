#list questions 1-10 
#Name: Premnath Sonkusare

#find smallest number of list
def find_smallest_number(nums:list)->int:
  smallest = float("inf")
  for num in nums:
    if num<smallest:
      smallest = num
  return smallest

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list

if __name__ == "__main__":
    
    #for smallest number of list
    input_list = list(input("Enter the numbers of a list").split(","))
    formatted_list = get_formatted_list(input_list)
    print(f"Given list is: {formatted_list}")
    smallest_num = find_smallest_number(formatted_list)
    print(f"smallest number of a list is:{smallest_num}")