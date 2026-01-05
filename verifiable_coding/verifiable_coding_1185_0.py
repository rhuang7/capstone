import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        s = int(data[idx])
        idx += 1
        f = int(data[idx])
        idx += 1
        missing = list(map(int, data[idx:idx + f]))
        idx += f
        torn = int(data[idx])
        idx += 1
        
        total_pages = 2 * s
        missing_set = set(missing)
        torn_leaves = torn
        
        # Calculate total sum of all pages
        total_sum = sum(range(1, total_pages + 1))
        
        # Calculate sum of missing pages
        missing_sum = sum(missing)
        
        # Calculate sum of pages on torn leaves
        torn_sum = 0
        for i in range(torn_leaves):
            page1 = 2 * i + 1
            page2 = 2 * i + 2
            if page1 in missing_set or page2 in missing_set:
                continue
            torn_sum += page1 + page2
        
        # Calculate expected sum
        expected_sum = total_sum - missing_sum - torn_sum
        results.append(f"{expected_sum:.4f}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()