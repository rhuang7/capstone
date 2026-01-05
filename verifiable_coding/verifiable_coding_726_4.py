import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        count = {}
        for _ in range(N):
            s = data[index]
            index += 1
            for c in s:
                count[c] = count.get(c, 0) + 1
        
        # Target counts for "codechef"
        target = {'c': 2, 'o': 1, 'd': 1, 'e': 2, 'h': 1, 'f': 1}
        res = float('inf')
        for key in target:
            if key not in count or count[key] < target[key]:
                res = 0
                break
            res = min(res, count[key] // target[key])
        
        print(res)

if __name__ == '__main__':
    solve()