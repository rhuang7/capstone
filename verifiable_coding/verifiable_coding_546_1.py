import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    D_list = list(map(int, data[1:T+1]))
    
    for D in D_list:
        if D == 0:
            print(0)
            continue
        count = 0
        while D > 0:
            max_pow = 1
            while max_pow * 2 <= D:
                max_pow *= 2
            count += 1
            D -= max_pow
        print(count)

if __name__ == '__main__':
    solve()