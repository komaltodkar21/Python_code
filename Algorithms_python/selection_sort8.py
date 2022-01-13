# find minimum element from the list of array
def find_min_element(arr):
    min = 100000000000
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
    return min

if __name__=='__main__':
    elements = [78,12,15,8,2,61,53,23,27]
    print(find_min_element(elements))


#selection sort
def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__=='__main__':
    elements = [78,12,15,8,2,61,53,23,27]
    selection_sort(elements)
    print(elements)


#selection sort using test cases
def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__=='__main__':
    tests = [
        [89,78,61,53,23,21,17,12,9,7,6,2,1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78,12,15,8,61,53,23,27],
        [5]
    ]
    
    for elements in tests:
        selection_sort(elements)
        print(elements)

