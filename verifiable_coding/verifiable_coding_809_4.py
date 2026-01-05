import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    A.sort(reverse=True)
    found = False
    result = []
    for i in range(N-2):
        if A[i] >= A[i+1] + A[i+2]:
            continue
        for j in range(i+1, N-1):
            if A[j] >= A[j+1] + A[i]:
                continue
            for k in range(j+1, N):
                if A[k] >= A[j] + A[i]:
                    continue
                result = [A[i], A[j], A[k]]
                found = True
                break
            if found:
                break
        if found:
            break
    if found:
        print("YES")
        print(f"{result[0]} {result[1]} {result[2]}")
    else:
        print("NO")