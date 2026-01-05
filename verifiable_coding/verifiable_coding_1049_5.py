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
        
        for i in range(n - k + 1):
            window = arr[i:i+k]
            unique = set(window)
            if len(unique) == len(window):
                current_sum = sum(window)
                if current_sum > max_sum:
                    max_sum = current_sum
        
        print(max_sum)

if __name__ == '__main__':
    solve()