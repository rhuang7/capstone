import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    A.sort()
    found = False
    result = []
    for i in range(N-1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if A[left] + A[left+1] > A[right]:
                result = [A[right], A[left+1], A[left]]
                found = True
                break
            elif A[left] + A[right] > A[left+1]:
                left += 1
            else:
                right -= 1
        if found:
            break
    if found:
        print("YES")
        print(f"{result[0]} {result[1]} {result[2]}")
    else:
        print("NO")