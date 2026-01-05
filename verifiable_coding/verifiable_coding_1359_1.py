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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        # Sort the array
        A.sort()
        # The minimum time is the sum of the differences between each element and the median, divided by 2
        # Because each operation can change a value by an odd number, and we can adjust any value to reach the median
        median = A[N//2]
        total = 0
        for num in A:
            total += abs(num - median)
        results.append(str(total // 2))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()