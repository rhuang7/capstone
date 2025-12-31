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
            largest_pow2 = 1 << (D.bit_length() - 1)
            if largest_pow2 == D:
                count += 1
                break
            count += 1
            D -= largest_pow2
        print(count)

if __name__ == '__main__':
    solve()