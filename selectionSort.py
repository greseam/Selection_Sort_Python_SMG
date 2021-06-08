array_unsort=[12,3,4,51,2,5,58,70,1,10,2]
sort_array=[]

def selection_Sort(array):
    print(array)
    count = len(array)
    while count > 0:
        element = findmin(array)
        sort_array.append(element)
        count=count-1
    print(sort_array)

def findmin(array):
    i = 0
    min = array[i]
    while i < len(array)-1:
        if min > array[i+1]:
            min = array[i+1]
            print("min="+str(min))
        i = i + 1
    array.remove(min)
    print("True min = "+str(min))
    return min

selection_Sort(array_unsort)