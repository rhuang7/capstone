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
            # Check if there is at least one island that can provide all required ingredients
            can_skip = False
            for i in range(N):
                island_ingredients = set()
                for j in range(int(data[idx]), idx + int(data[idx])):
                    island_ingredients.add(int(data[j]))
                if required.issubset(island_ingredients):
                    can_skip = True
                    break
            if can_skip:
                results.append("some")
            else:
                results.append("all")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()