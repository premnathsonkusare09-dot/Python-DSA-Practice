#Mixed Problems 25-50
#Name: Premnath Sonkusare

def check_balance_brackets(problem:str)->bool:
  count_sq_bracket=0
  count_sm_bracket=0
  count_cr_bracket=0
  for ch in problem:
    if ch =="[":
      count_sq_bracket +=1
    if ch =="]":
      count_sq_bracket -=1
    if ch =="(":
      count_sm_bracket +=1
    if ch ==")":
      count_sm_bracket -=1
    if ch =="{":
      count_cr_bracket +=1
    if ch =="}":
      count_cr_bracket -=1
  if(count_sq_bracket==0 and count_sm_bracket==0 and count_cr_bracket==0):
      return True
  return False

if __name__ == "__main__":
    try:
        input_brackets = str(input("Enter the Brackets({}()[]):"))
        is_balanced = check_balance_brackets(input_brackets)
        print(f"Given bracket is Balanced bracket:{is_balanced}")
    except Exception as e:
       print(type(e).__name__)
       print(str(e))