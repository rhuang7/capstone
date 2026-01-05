import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        A = list(map(int, data[index:index + N]))
        index += N
        
        total = sum(A)
        if total % N == 0:
            results.append("Yes")
        else:
            results.append("No")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()