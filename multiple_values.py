# Function in python can return more than one variable without the need for a dictionary
# a list, or class.

# with condition if val is not find
def get_index_of_value(thelist, value):
    for index, val in enumerate(thelist):
        if value == val:
            return True, index
    
    return False, None

if __name__ == "__main__":
    mylist = [i for i in range(10,100)]
    try:
        val = int(input("input number only: "))
        cond, index = get_index_of_value(mylist, val)
        if cond == True:
            print(f"index of {val} from list is", index)
        else:
            print(f"not found {val} in list")
    except Exception as error:
        print("Error : {}".format(error))
        print("Only Number!")