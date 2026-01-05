import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        arr = list(map(int, data[idx:idx+n]))
        idx += n
        
        max_sum = -float('inf')
        seen = set()
        current_sum = 0
        
        for i in range(k):
            current_sum += arr[i]
            seen.add(arr[i])
        
        max_sum = current_sum
        
        for i in range(k, n):
            out = arr[i - k]
            in_ = arr[i]
            current_sum += in_ - out
            if in_ in seen:
                while out in seen:
                    seen.remove(out)
                    out = arr[i - k]
                    i -= 1
                seen.add(in_)
            else:
                seen.add(in_)
            max_sum = max(max_sum, current_sum)
        
        print(max_sum)

if __name__ == '__main__':
    solve()