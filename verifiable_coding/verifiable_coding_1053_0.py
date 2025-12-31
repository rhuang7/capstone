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
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Find transition point in sorted array
        # All 0s come before all 1s
        # So find the first occurrence of 1
        transition_point = 0
        while transition_point < N and arr[transition_point] == 0:
            transition_point += 1
        
        results.append(str(transition_point))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()