#list questions 1-10 
#Name: Premnath Sonkusare

#find merge sorted list
def find_merge_sorted_list(L1:list,L2:list)->list:
  merge_list = list()
  i1 = 0
  i2 = 0
  while i1<len(L1) and i2<len(L2):
    if L1[i1]<L2[i2]:
      merge_list.append(L1[i1])
      i1 += 1 
    else :
      merge_list.append(L2[i2])
      i2 += 1 
  while i1<len(L1):
      merge_list.append(L1[i1])
      i1 += 1
  while i2<len(L2):
      merge_list.append(L2[i2])
      i2 += 1 
  return merge_list
  
 #get formatted list
def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list
     
if __name__ == "__main__":
    
    #for merge list 
    input_list = list(input("Enter the numbers of a list1:").split(","))
    formatted_list1 = get_formatted_list(input_list)
    print(f"Given list1 is: {formatted_list1}")
    input_list = list(input("Enter the numbers of a list2:").split(","))
    formatted_list2 = get_formatted_list(input_list)
    print(f"Given list2 is: {formatted_list2}")
    merge_list = find_merge_sorted_list(formatted_list1,formatted_list2)
    print(f"Merge list is: {merge_list}")
    