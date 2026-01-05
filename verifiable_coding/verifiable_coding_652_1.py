import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        s1 = data[index].lower()
        s2 = data[index+1].lower()
        index += 2
        
        if s1 < s2:
            print("first")
        elif s1 > s2:
            print("second")
        else:
            print("equal")

if __name__ == '__main__':
    solve()