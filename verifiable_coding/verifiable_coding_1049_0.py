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
        
        max_sum = -float('inf')
        seen = set()
        
        for i in range(n - k + 1):
            window = arr[i:i+k]
            seen.clear()
            current_sum = 0
            distinct = True
            for num in window:
                if num in seen:
                    distinct = False
                    break
                seen.add(num)
                current_sum += num
            if distinct:
                if current_sum > max_sum:
                    max_sum = current_sum
        
        print(max_sum)

if __name__ == '__main__':
    solve()