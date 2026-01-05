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
        S = int(data[idx+2])
        idx += 3
        H = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the hours in ascending order
        H.sort()
        
        count = 0
        i = 0
        while i < N and count < M:
            # Check if the current topic can be covered in one day
            if H[i] <= S:
                count += 1
                i += 1
            else:
                # Check if the current topic can be covered in two days
                if H[i] <= 2 * S:
                    count += 1
                    i += 1
                else:
                    # Cannot cover this topic
                    i += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()