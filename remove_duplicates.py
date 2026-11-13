
#removing duplicate values of a list
def get_unique_list(nums:list)->list:
  unique_list = list()
  for num in nums:
    if num not in unique_list:
      unique_list.append(num)
  return unique_list

 #get formatted list
def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list
     
if __name__ == "__main__":

    #for removing duplicates or get unique list
    input_list = list(input("Enter the numbers of a list").split(","))
    formatted_list = get_formatted_list(input_list)
    print(f"Given list is: {formatted_list}")
    unique_list = get_unique_list(formatted_list)
    print(f"Unique list is: {unique_list}")