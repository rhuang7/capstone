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
        
        max_sum = -1
        seen = set()
        current_sum = 0
        
        for i in range(n):
            if i >= k:
                if arr[i] in seen:
                    seen.remove(arr[i - k])
                seen.add(arr[i])
                current_sum -= arr[i - k]
                current_sum += arr[i]
            else:
                seen.add(arr[i])
                current_sum += arr[i]
            
            if len(seen) == k:
                max_sum = max(max_sum, current_sum)
        
        print(max_sum)

if __name__ == '__main__':
    solve()