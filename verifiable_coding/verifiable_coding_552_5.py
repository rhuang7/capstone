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
        W = list(map(int, data[idx:idx+N]))
        idx += N
        W.sort()
        total = sum(W)
        # The son takes the K lightest items, Chef takes the rest
        son_weight = sum(W[:K])
        chef_weight = total - son_weight
        results.append(str(chef_weight - son_weight))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()