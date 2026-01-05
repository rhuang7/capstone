import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    strengths = list(map(int, data[1:]))
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += abs(strengths[i] - strengths[j])
    print(total)

if __name__ == '__main__':
    solve()