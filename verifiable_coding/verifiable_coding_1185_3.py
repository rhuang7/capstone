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
        t_leaves = int(data[idx])
        idx += 1
        
        total_pages = 2 * s
        pages = set(range(1, total_pages + 1))
        
        for page in missing:
            if 1 <= page <= total_pages:
                pages.discard(page)
        
        removed_pages = set()
        for i in range(t_leaves):
            if i * 2 + 1 <= total_pages:
                removed_pages.add(i * 2 + 1)
                removed_pages.add(i * 2 + 2)
        
        remaining_pages = pages - removed_pages
        
        if not remaining_pages:
            results.append("0.0000")
            continue
        
        sum_pages = sum(remaining_pages)
        count_pages = len(remaining_pages)
        expected = sum_pages / count_pages
        results.append(f"{expected:.4f}")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()