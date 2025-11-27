def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr

    mid_Element = arr[len(arr)//2]

    #Here take same name which takin after for to assign in newvalue for variable    
    left_side = [item for item in arr if item < mid_Element]
    middle = [item for item in arr if item == mid_Element]
    right_side = [item for item in arr if item > mid_Element]

    #we cant take left or right , only take with function(left) or function(right)
    return Quick_Sort(left_side) + middle + Quick_Sort(right_side)


def main():
    User = input("enter values: ")
    arr = list(map(int,User.split()))
    newArr = Quick_Sort(arr)
    print("Sorted list:", newArr)


main()
