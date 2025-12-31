import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        students = [10] * N
        for _ in range(M):
            i = int(data[idx])
            j = int(data[idx+1])
            k = int(data[idx+2])
            idx += 3
            for x in range(i-1, j):
                students[x] *= k
        total = sum(students)
        mean = total // N
        results.append(str(mean))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()