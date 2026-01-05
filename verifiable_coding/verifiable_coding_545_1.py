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
        for _ in range(N):
            Pi = int(data[idx])
            idx += 1
            for i in range(Pi):
                ingredients.add(int(data[idx]))
                idx += 1
        if required - ingredients:
            results.append("sad")
        else:
            # Check if there is at least one island that can provide all ingredients
            # If yes, then "some" else "all"
            has_all = False
            for i in range(N):
                Pi = int(data[idx])
                idx += 1
                found = set()
                for j in range(Pi):
                    found.add(int(data[idx]))
                    idx += 1
                if found == required:
                    has_all = True
                    break
            if has_all:
                results.append("all")
            else:
                results.append("some")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()