import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    H_list = data[1:T+1]

    for H in H_list:
        if len(H) == 0:
            print(0)
            continue
        a_count = H.count('a')
        b_count = H.count('b')
        print(1 if a_count == 0 or b_count == 0 else 2)

if __name__ == '__main__':
    solve()