import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        L = int(data[index])
        R = int(data[index+1])
        index += 2
        count = 0
        for num in range(L, R + 1):
            if num % 10 in {2, 3, 9}:
                count += 1
        print(count)

if __name__ == '__main__':
    solve()