def squareNumber(array1):
    n = len(array1)
    new_array = [0]*n
    for i in range(len(new_array)):
        new_array[i] = array1[i] ** 2
    new_array.sort()
    return new_array
print(squareNumber([1, 2, 0, 6, -5]))
print(squareNumber([]))