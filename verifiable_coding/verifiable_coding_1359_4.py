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
        # Because each operation can change a temperature by an odd number, so we need to make all temperatures equal to the first one
        # But since we can add or subtract any odd number, we can make all temperatures equal to the first one in (sum of absolute differences) // 2 seconds
        # Because each operation can change a temperature by an odd number, which is equivalent to changing the difference by an even number
        # So the minimum time is the sum of absolute differences between each element and the first element, divided by 2
        total = 0
        for i in range(1, N):
            total += abs(A[i] - A[0])
        results.append(str(total // 2))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()