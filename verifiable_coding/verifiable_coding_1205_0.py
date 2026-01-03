import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i]
        n = len(S)
        total = 0
        
        for L in range(n):
            for R in range(L, n):
                U = list(S)
                for j in range(L, R + 1):
                    U[j] = '1' if U[j] == '0' else '0'
                count = 0
                for k in range(n - 1):
                    if U[k] == U[k + 1]:
                        count += 1
                total += count
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()