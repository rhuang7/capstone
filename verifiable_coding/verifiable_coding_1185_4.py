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
        
        total_pages = 2 * s
        missing_pages = set(f_list)
        
        # Calculate total sum of all pages
        total_sum = sum(range(1, total_pages + 1))
        
        # Calculate sum of missing pages
        missing_sum = sum(missing_pages)
        
        # Calculate sum of pages removed by leaves
        removed_sum = 0
        for i in range(t_leaves):
            page = 2 * i + 1
            removed_sum += page
            removed_sum += page + 1
        
        # Calculate sum of pages left
        left_sum = total_sum - missing_sum - removed_sum
        
        # Calculate expected value
        expected = left_sum / (total_pages - len(missing_pages) - 2 * t_leaves)
        results.append("{0:.4f}".format(expected))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()