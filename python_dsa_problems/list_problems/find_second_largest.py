#list questions 1-10 
#Name: Premnath Sonkusare

# #find second largest number of list
def find_second_largest_num(nums:list)->int:
  largest = float('-inf')
  second_largest = float('-inf')
  if len(nums)==0:
    raise ValueError("list have no values!")
  for num in nums:
    if num>largest:
      second_largest = largest
      largest = num
    elif num<largest and num>second_largest:
      second_largest = num
  if second_largest == float('-inf'):
    raise ValueError("Second largest doe not exist!")
  if largest == second_largest:
    raise ValueError("List must have distinct values!")
  return second_largest

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list
     
if __name__ == "__main__":

    #for finding a second largest Value
    input_list = list(input("Enter the numbers of a list").split(","))
    formatted_list = get_formatted_list(input_list)
    print(f"Given list is: {formatted_list}")
    sec_largest = find_second_largest_num(formatted_list)
    print(f"SEcond largest value is:{sec_largest}")
    