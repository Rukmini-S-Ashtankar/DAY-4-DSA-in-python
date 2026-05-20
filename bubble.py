def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):   # by deault value of j is 0 # j = 0      #-i is included so that after one iteration it won't go on the largest element again. won't go on last position then last 2nd and so on
            if array[j] >array[j+1]:                           #-i will reduce the internal time complexity
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            print(array)
        print()

array = [64,34,25,12,22,11,90]
bubbleSort(array)