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
        ingredients = set()
        required = set(range(1, K+1))
        all_required = False
        for _ in range(N):
            Pi = int(data[idx])
            idx += 1
            for i in range(Pi):
                ingredients.add(int(data[idx]))
                idx += 1
        if required - ingredients:
            results.append("sad")
        else:
            all_required = True
            for i in range(N):
                temp = set()
                for j in range(i, N):
                    temp.update(data[idx:idx+data[idx]])
                    idx += data[idx]
                    if temp.issuperset(required):
                        all_required = False
                        break
                if not all_required:
                    break
            if all_required:
                results.append("all")
            else:
                results.append("some")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()