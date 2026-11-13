 #list questions 1-10 
#Name: Premnath Sonkusare

#Count a target value
def count_target_value(nums:list,target:int)->int:
  target_count = 0
  for num in nums:
    if num==target:
      target_count+=1
  return target_count

 #get formatted list
def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list
     
if __name__ == "__main__":

     #for count a target values
       input_list = list(input("Enter the numbers of a list").split(","))
       formatted_list = get_formatted_list(input_list)
       print(f"Given list is: {formatted_list}")
       target_value = int(input("Enter Target Value:"))
       target_count = count_target_value(formatted_list,target_value)
       print(f"Target count of {target_value} is: {target_count}")