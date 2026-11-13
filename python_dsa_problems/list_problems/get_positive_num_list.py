#list questions 1-10 
#Name: Premnath Sonkusare

# #keep positive number of list
def find_positive_nums(nums:list)->list:
  positive_num_list = list()
  for num in nums:
    if num>0:
      positive_num_list.append(num)
  return positive_num_list

 #get formatted list
def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list
     
if __name__ == "__main__":

    #for positive number list
       input_list = list(input("Enter the numbers of a list").split(","))
       formatted_list = get_formatted_list(input_list)
       print(f"Given list is: {formatted_list}")
       pos_num_list = find_positive_nums(formatted_list)
       print(f"Positive number list is:{pos_num_list}")