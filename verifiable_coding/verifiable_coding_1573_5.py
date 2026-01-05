import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    test_cases = list(map(int, data[1:T+1]))
    
    for N in test_cases:
        if N % 2 == 0:
            print("NO")
            continue
        
        print("YES")
        for i in range(N):
            row = ['0'] * N
            for j in range(N):
                if i < j:
                    row[j] = '1'
                elif i > j:
                    row[i] = '1'
            print(''.join(row))
            
if __name__ == '__main__':
    solve()