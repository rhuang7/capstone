import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        # The largest number <= c that leaves remainder b when divided by a is c - ((c - b) % a)
        # But if (c - b) < 0, then the number is b
        if c < b:
            results.append(b)
        else:
            results.append(c - ((c - b) % a))
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()