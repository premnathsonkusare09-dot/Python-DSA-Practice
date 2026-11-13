#Maths questions 11-25
#Name: Premnath Sonkusare

def manhattan_distance(first: tuple[int, int], second: tuple[int, int]) -> int:
    if len(first)==2 and len(second)==2:
        return abs(first[0] - second[0]) + abs(first[1] - second[1])
    else:
        raise ValueError("Cordinate are not supported, Enter 2 Cordinates Only for both the points!")

def get_formatted_list(nums:list)->list:
    formatted_list = list()
    for num in nums:
        formatted_list.append(int(num))
    return formatted_list

if __name__ == "__main__":
    try:
       
        first_input_cordinate = list(input("Enter Point 1 Cordinate(x,y):").split(","))
        second_input_cordinate = list(input("Enter Point 2 Cordinate(x,y):").split(","))
        point_1 = get_formatted_list(first_input_cordinate)
        point_2 = get_formatted_list(second_input_cordinate)
        man_dis = manhattan_distance(point_1,point_2)
        print(f"Manhattan Distance of {point_1} and {point_2} is : {man_dis}")

    except Exception as e:
        print(type(e).__name__)
        print(str(e))
