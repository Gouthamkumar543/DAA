def Sorting_Elements(x):
    n = len(x)
    for i in range(n):
        index = i
        for j in range(i+1,n):
            if x[j] < x[index]:
                index = j
        x[i],x[index] = x[index],x[i]


def Goutham():
    user = input("enter numbers in space formate: ")
    arr = list(map(int,user.split()))
    Sorting_Elements(arr)
    print("Shorted list:",arr)


Goutham()
