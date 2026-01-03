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
        # The minimum time is the sum of the differences between each element and the first element, divided by 2
        # Because each operation can change a temperature by an odd number, and we can adjust any temperature
        # So the minimum time is the sum of the absolute differences between each element and the first element
        total = 0
        for i in range(1, N):
            total += abs(A[i] - A[0])
        results.append(str(total))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()