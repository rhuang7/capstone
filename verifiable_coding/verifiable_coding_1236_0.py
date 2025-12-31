import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        count = 0
        i = 0
        while i < n - 1:
            if s[i] == s[i + 1]:
                count += 1
            i += 1
        
        print(count)

if __name__ == '__main__':
    solve()