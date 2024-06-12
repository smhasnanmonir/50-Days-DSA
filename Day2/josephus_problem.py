def winner(arr,k):
    arr = [i+1 for i in range(arr)]
    def helper(arr, start_index):
        if len(arr) == 1:
            return arr[0]
        #recursive case
        index_to_remove = (start_index+ k-1)%len(arr)
        # print(arr.pop(index_to_remove))
        arr.pop(index_to_remove)
        return helper(arr, index_to_remove)
    return helper(arr, 0)

print(winner(5,4))

def winner2(n,k):
    def josephus(n):
        if n == 1:
            return 0
        return (josephus(n-1)+k)%n
    return josephus(n)+1
print(winner2(5,4))