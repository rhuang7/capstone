import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        J = data[index]
        S = data[index + 1]
        index += 2
        
        count = 0
        for char in S:
            if char in J:
                count += 1
        print(count)
        
if __name__ == '__main__':
    solve()