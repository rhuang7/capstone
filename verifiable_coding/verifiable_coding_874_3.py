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
        N, M, S = map(int, data[idx:idx+3])
        idx += 3
        H = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the hours in ascending order
        H.sort()
        
        count = 0
        i = 0
        while i < N and count < M:
            # Check if the current topic can be done in one day
            if H[i] <= S:
                count += 1
                i += 1
            else:
                # Check if the current topic can be done in two days
                if H[i] <= 2 * S:
                    count += 1
                    i += 1
                else:
                    # Cannot do this topic at all
                    i += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()