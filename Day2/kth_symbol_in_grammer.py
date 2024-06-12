def kth_symbol(num,k):
    m_len = 2**(num-1) 
    mid_value = m_len//2
    if k>(m_len):
        return "invalid"
    if num == 1:
        return 0
    elif k<=mid_value:
        return kth_symbol(num-1,k)
    else:
        return 1 - kth_symbol(num-1, k-mid_value)
print(kth_symbol(4,7))
print(kth_symbol(4,8))
print(kth_symbol(4,9))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


