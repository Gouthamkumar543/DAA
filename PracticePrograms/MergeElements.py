def Merging_Elements(x):
    
    if len(x) > 1:
        midValue = len(x)//2
        leftSideValues = x[:midValue]
        rightSideValues = x[midValue:]

        Merging_Elements(leftSideValues)
        Merging_Elements(rightSideValues)

        i=j=k=0

        while i < len(leftSideValues) and j < len(rightSideValues):
            if leftSideValues[i] < rightSideValues[j]:
                x[k] = leftSideValues[i]
                i += 1
            else:
                x[k] = rightSideValues[j]
                j +=1
            k +=1
            

        while i < len(leftSideValues):
            x[k] = leftSideValues[i]
            i +=1
            k += 1

            
        while j < len(rightSideValues):
            x[k] = rightSideValues[j]
            j += 1
            k += 1



def Goutham():
    User = input("Enter Values: ")
    arr = list(map(int,User.split()))
    Merging_Elements(arr)
    print("merge list: ",arr)



Goutham()
