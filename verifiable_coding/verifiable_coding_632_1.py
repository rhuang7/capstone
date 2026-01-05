import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        k = int(data[index+1])
        index += 2
        if N == 1:
            if k % 2 == 1:
                print("ON")
            else:
                print("OFF")
            continue
        on_count = 0
        for i in range(1, N):
            if k >= i:
                on_count += 1
            else:
                break
        if on_count == N - 1 and k % 2 == 1:
            print("ON")
        else:
            print("OFF")

if __name__ == '__main__':
    solve()