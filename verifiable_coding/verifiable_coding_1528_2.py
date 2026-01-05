import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        coins = data[idx:idx+N]
        idx += N
        heads = 0
        flip = False
        for i in range(N-1, -1, -1):
            if flip:
                if coins[i] == 'H':
                    heads -= 1
                else:
                    heads += 1
            else:
                if coins[i] == 'H':
                    heads += 1
            if K > 0:
                K -= 1
                if K == 0:
                    break
            if K > 0:
                flip = not flip
        results.append(str(heads))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()