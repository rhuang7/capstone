import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        X = int(data[index])
        N = int(data[index+1])
        index += 2
        count = N // X
        sum = (count * (count + 1)) // 2 * X
        print(sum)

if __name__ == '__main__':
    solve()