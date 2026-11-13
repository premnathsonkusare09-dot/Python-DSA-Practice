#Mixed Problems 25-50
#Name: Premnath Sonkusare

def build_prefix_sum(nums:list[int])->list:
  ans = list()
  ans.append(nums[0])
  for index in range(1,len(nums)):
    ans.append(ans[index-1]+nums[index])
  return ans

def get_formatted_list(nums:list)->list:
     formatted_list = list()
     for num in nums:
         formatted_list.append(int(num))
     return formatted_list

if __name__ == "__main__":
    try:
        input_list = list(input("Enter the numbers of list:").split(","))
        form_list = get_formatted_list(input_list)
        prefix_sum_list = build_prefix_sum(form_list)
        print(f"Builded prefix sum list is:{prefix_sum_list}")    
    except Exception as e:
           print(type(e).__name__)
           print(str(e))
            