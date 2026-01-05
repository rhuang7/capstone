import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        if K <= N:
            results.append(K)
        else:
            base = K // N
            remainder = K % N
            if remainder == 0:
                results.append(base)
            else:
                results.append(base)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()