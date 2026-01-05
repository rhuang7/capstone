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
        f_count = int(data[idx])
        idx += 1
        missing = list(map(int, data[idx:idx + f_count]))
        idx += f_count
        t_leaves = int(data[idx])
        idx += 1
        
        total_pages = s * 2
        missing_set = set(missing)
        removed_pages = set()
        
        for leaf in range(t_leaves):
            removed_pages.add(2 * leaf + 1)
            removed_pages.add(2 * leaf + 2)
        
        present_pages = set()
        for page in range(1, total_pages + 1):
            if page not in missing_set and page not in removed_pages:
                present_pages.add(page)
        
        expected_sum = sum(present_pages) / (len(present_pages) if present_pages else 1)
        results.append("{0:.4f}".format(expected_sum))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()