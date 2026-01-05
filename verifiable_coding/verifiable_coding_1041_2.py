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
        S = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_val = -float('inf')
        start = 0
        end = 0
        
        for i in range(N):
            current_val = 1
            for j in range(i, N):
                current_val *= S[j]
                if current_val > max_val:
                    max_val = current_val
                    start = i
                    end = j
                elif current_val == max_val:
                    if i > start or (i == start and j > end):
                        start = i
                        end = j
        
        results.append(f"{max_val} {start} {end}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()