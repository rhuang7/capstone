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
        
        max_sum = -float('inf')
        current_sum = 0
        start = 0
        end = 0
        min_length = N
        
        for i in range(N):
            current_sum += A[i]
            if current_sum > max_sum:
                max_sum = current_sum
                start = i + 1
                end = i + 1
                min_length = 1
            elif current_sum == max_sum:
                if (i + 1 - start + 1) < min_length:
                    min_length = i + 1 - start + 1
                    end = i + 1
        
        results.append(str(min_length))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()