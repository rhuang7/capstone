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
        all_collected = False
        for _ in range(N):
            Pi = int(data[idx])
            idx += 1
            for i in range(Pi):
                ingredients.add(int(data[idx]))
                idx += 1
        if required - ingredients:
            results.append("sad")
        else:
            # Check if there is at least one island that can be skipped
            # We need to check if there is a subset of islands that can collect all K ingredients
            # We can do this by checking if there is an island that has all K ingredients
            # If not, then we need to check if there is a way to skip some islands
            # For this, we can try to remove each island and check if the remaining can collect all K
            # But for large N, this is O(N^2), which is not feasible
            # So we can do the following:
            # Keep track of all the ingredients collected
            # Then, for each island, check if removing it would still allow all K to be collected
            # If there is at least one such island, then answer is "some"
            # Else, answer is "all"
            # To optimize, we can track the count of each ingredient
            # And for each island, check if removing it would decrease the count of any ingredient
            # If not, then it can be skipped
            # So we can do this:
            from collections import defaultdict
            count = defaultdict(int)
            for i in range(N):
                Pi = int(data[idx])
                idx += 1
                for j in range(Pi):
                    count[int(data[idx])] += 1
                    idx += 1
            # Check if there is an island that can be skipped
            can_skip = False
            for i in range(N):
                Pi = int(data[idx])
                idx += 1
                for j in range(Pi):
                    count[int(data[idx])] -= 1
                    idx += 1
                # Check if all K ingredients are still present
                all_present = True
                for k in range(1, K+1):
                    if count[k] == 0:
                        all_present = False
                        break
                if all_present:
                    can_skip = True
                    break
                # Restore the count
                for j in range(Pi):
                    count[int(data[idx])] += 1
                    idx += 1
            if can_skip:
                results.append("some")
            else:
                results.append("all")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()