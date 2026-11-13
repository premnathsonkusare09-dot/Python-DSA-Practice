#list questions 1-10 
#Name: Premnath Sonkusare

#find sum of all numbers of list
def find_sum_all_numbers(nums:list)->int:
  total_sum = 0
  for num in nums:
    total_sum +=num
  return total_sum

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list

if __name__ == "__main__":

 #for total sum
    input_list = list(input("Enter the numbers of a list").split(","))
    formatted_list = get_formatted_list(input_list)
    print(f"Given list is: {formatted_list}")
    total_sum = find_sum_all_numbers(formatted_list)
    print(f"Total sum of the list is:{total_sum}")