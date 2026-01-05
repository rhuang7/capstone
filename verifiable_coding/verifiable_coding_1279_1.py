import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        X = []
        Y = []
        x_count = collections.defaultdict(list)
        y_sum = collections.defaultdict(int)
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx + 1])
            idx += 2
            X.append(x)
            Y.append(y)
            x_count[x].append(y)
            y_sum[x] += y
        
        max_res = 0
        for x1 in x_count:
            for x2 in x_count:
                if x1 == x2:
                    continue
                for x3 in x_count:
                    if x1 == x3 or x2 == x3:
                        continue
                    current_sum = y_sum[x1] + y_sum[x2] + y_sum[x3]
                    if current_sum > max_res:
                        max_res = current_sum
        results.append(max_res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()