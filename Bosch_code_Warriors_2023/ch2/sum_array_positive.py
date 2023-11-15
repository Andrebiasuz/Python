def positive_sum(arr):
    return sum([i for i in arr if i >= 0])
   


print(positive_sum([-1,-5,-2,-4,-8,-4,-5]))

''' sum = 0
   arr_2 = filter(lambda x: x >= 0, arr)
   print(' '.join(map(str, arr_2))) '''