import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        if N % 2 == 0:
            print("NO")
            continue
        print("YES")
        for i in range(N):
            row = ['0'] * N
            for j in range(N):
                if i != j:
                    if (i + j) % 2 == 0:
                        row[j] = '1'
                    else:
                        row[j] = '0'
            print(''.join(row))
        
if __name__ == '__main__':
    solve()