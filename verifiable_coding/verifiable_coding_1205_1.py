import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    S_list = data[1:T+1]
    
    for S in S_list:
        n = len(S)
        total = 0
        for i in range(n):
            for j in range(i, n):
                U = list(S)
                for k in range(i, j+1):
                    U[k] = '1' if U[k] == '0' else '0'
                count = 0
                for m in range(n-1):
                    if U[m] == U[m+1]:
                        count += 1
                total += count
        print(total)

if __name__ == '__main__':
    solve()