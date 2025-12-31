import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        count = {'c': 0, 'o': 0, 'd': 0, 'e': 0, 'h': 0, 'f': 0}
        for _ in range(N):
            s = data[idx]
            idx += 1
            for c in s:
                if c in count:
                    count[c] += 1
        # Calculate the maximum number of "codechef" meals
        min_count = min(count['c'], count['o'], count['d'], count['e'], count['h'], count['f'])
        print(min_count)
        
if __name__ == '__main__':
    solve()