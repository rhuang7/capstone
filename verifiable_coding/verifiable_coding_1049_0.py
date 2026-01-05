import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        n, k = int(data[index]), int(data[index+1])
        index += 2
        arr = list(map(int, data[index:index+n]))
        index += n
        
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