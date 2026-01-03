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
        torn = int(data[idx])
        idx += 1
        
        total_pages = 2 * s
        missing_set = set(missing)
        torn_pages = set()
        
        for i in range(1, total_pages + 1, 2):
            if i in missing_set:
                continue
            if (i + 1) <= total_pages:
                if (i + 1) in missing_set:
                    continue
                torn_pages.add(i)
                torn_pages.add(i + 1)
        
        if torn > 0:
            for i in range(1, total_pages + 1, 2):
                if i in missing_set:
                    continue
                if (i + 1) <= total_pages:
                    if (i + 1) in missing_set:
                        continue
                    if torn > 0:
                        torn_pages.add(i)
                        torn_pages.add(i + 1)
                        torn -= 1
        
        sum_left = 0
        for i in range(1, total_pages + 1, 2):
            if i in missing_set:
                continue
            if (i + 1) <= total_pages:
                if (i + 1) in missing_set:
                    continue
            if i not in torn_pages:
                sum_left += i
            if (i + 1) <= total_pages and (i + 1) not in torn_pages:
                sum_left += i + 1
        
        expected = sum_left / (total_pages - len(missing_set) - torn * 2)
        results.append("{0:.4f}".format(expected))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()