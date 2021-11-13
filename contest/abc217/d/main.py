import bisect
from array import array
def MI(): return map(int, input().split())


L, Q = MI()
arr = array("i", [0, L])
for i in range(Q):
    c, x = MI()
    if c == 1:
        bisect.insort(arr, x)
    elif c == 2:
        id = bisect.bisect_left(arr, x)
        print(arr[id]-arr[id-1])
