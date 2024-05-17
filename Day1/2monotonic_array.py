def monotonic_Array(a):
    n = len(a)
    first_number = a[0]
    last_number = a[n-1]

    if first_number<last_number:
        for i in range(n-1):
            if a[i] > a[i+1]:
                return False
    elif first_number == last_number:
        for i in range(n-1):
            if a[i] != a[i+1]:
                return False
    else:
        for i in range(n-1):
            if a[i] < a[i+1]:
                return False
    return True

print(monotonic_Array([3, 4, 5, 6, 7]))
print(monotonic_Array([3, 3, 3, 3, 3]))
print(monotonic_Array([3, 2, 1, -2, -3]))
print(monotonic_Array([3, 2, 1, -2, 4]))