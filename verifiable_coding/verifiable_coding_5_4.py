import sys
import bisect
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        freq = defaultdict(int)
        for num in a:
            freq[num] += 1
        
        # Check if there is a possible split
        possible = False
        for l1 in range(1, n):
            l2 = n - l1
            # Check if the first l1 elements form a permutation of 1..l1
            # Check if the last l2 elements form a permutation of 1..l2
            # Check if all elements in first l1 are unique and in 1..l1
            # Check if all elements in last l2 are unique and in 1..l2
            # Also, check that the total count of each number is correct
            # For the first l1 elements
            valid1 = True
            cnt1 = defaultdict(int)
            for i in range(l1):
                num = a[i]
                if num < 1 or num > l1:
                    valid1 = False
                    break
                cnt1[num] += 1
            if not valid1:
                continue
            for num in cnt1:
                if cnt1[num] != 1:
                    valid1 = False
                    break
            if not valid1:
                continue
            # For the last l2 elements
            valid2 = True
            cnt2 = defaultdict(int)
            for i in range(l1, n):
                num = a[i]
                if num < 1 or num > l2:
                    valid2 = False
                    break
                cnt2[num] += 1
            if not valid2:
                continue
            for num in cnt2:
                if cnt2[num] != 1:
                    valid2 = False
                    break
            if valid1 and valid2:
                possible = True
                results.append(f"{l1} {l2}")
                break
        
        if possible:
            results.append(str(len(results)))
            results.extend(results[-1:])
        else:
            results.append("0")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()