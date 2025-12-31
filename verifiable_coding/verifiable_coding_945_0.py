import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        max_remainder = 0
        best_A = 1
        
        for A in range(1, N + 1):
            remainder = N % A
            if remainder > max_remainder or (remainder == max_remainder and A > best_A):
                max_remainder = remainder
                best_A = A
        
        results.append(str(best_A))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()