import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        a = int(data[index])
        d = int(data[index+1])
        k = int(data[index+2])
        n = int(data[index+3])
        inc = int(data[index+4])
        index += 5
        
        current_d = d
        day = 1
        
        while day < n:
            day += 1
            if day % k == 0:
                current_d += inc
        
        print(current_d + (n - 1) * current_d)

if __name__ == '__main__':
    solve()