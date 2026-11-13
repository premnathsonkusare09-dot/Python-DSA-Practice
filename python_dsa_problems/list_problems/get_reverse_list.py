#list questions 1-10 
#Name: Premnath Sonkusare

# #reverse a list
def  get_reverse_list(nums:list)->list:
  reverse_list = list()
  for num in range(len(nums)-1,-1,-1):
    reverse_list.append(nums[num])
  return reverse_list
  #return nums[::-1]

   #get formatted list
def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list
     
if __name__ == "__main__":
    
       #for reverse a list
       input_list = list(input("Enter the numbers of a list").split(","))
       formatted_list = get_formatted_list(input_list)
       print(f"Given list is: {formatted_list}")
       reverse_list = get_reverse_list(formatted_list)
       print(f"Reverse list is: {reverse_list}")