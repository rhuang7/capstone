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
        max_len = 0
        
        for i in range(N):
            current_sum += A[i]
            if current_sum > max_sum:
                max_sum = current_sum
                max_len = i - start + 1
                end = i
            elif current_sum == max_sum:
                if (i - start + 1) > max_len:
                    max_len = i - start + 1
                    end = i
            if current_sum < 0:
                current_sum = 0
                start = i + 1
        
        results.append(str(max_len))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()