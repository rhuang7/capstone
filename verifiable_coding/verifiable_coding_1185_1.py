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
        f_list = list(map(int, data[idx:idx + f_count]))
        idx += f_count
        t_leaves = int(data[idx])
        idx += 1
        
        total_pages = s * 2
        missing_pages = set(f_list)
        removed_pages = set()
        
        for leaf in range(t_leaves):
            removed_pages.add(2 * leaf + 1)
            removed_pages.add(2 * leaf + 2)
        
        remaining_pages = []
        for page in range(1, total_pages + 1):
            if page not in missing_pages and page not in removed_pages:
                remaining_pages.append(page)
        
        expected_sum = sum(remaining_pages) / len(remaining_pages) if remaining_pages else 0.0
        results.append("{0:.4f}".format(expected_sum))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()