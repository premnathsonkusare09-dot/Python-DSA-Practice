#list questions 1-10 
#Name: Premnath Sonkusare

# #count even number of list 
def count_even_numbers(nums:list)->int:
  even_count = 0
  for num in nums:
    if num%2 == 0:
      even_count += 1
  return even_count

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list

if __name__ == "__main__":

    #for couting a even number of a list
    input_list = list(input("Enter the numbers of a list").split(","))
    formatted_list = get_formatted_list(input_list)
    print(f"Given list is: {formatted_list}")
    even_count = count_even_numbers(formatted_list)
    print(f"Even number count is:{even_count}")