import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        index += 2
        
        if a == b:
            print(0)
            continue
        
        diff = abs(b - a)
        count = 0
        
        # Use as many 5s as possible
        count += diff // 5
        diff %= 5
        
        # Use as many 2s as possible
        count += diff // 2
        diff %= 2
        
        # The remaining is 1s
        count += diff
        
        print(count)

if __name__ == '__main__':
    solve()