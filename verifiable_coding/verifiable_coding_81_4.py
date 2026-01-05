import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        a = data[index]
        b = data[index+1]
        c = data[index+2]
        index += 3
        
        possible = True
        for i in range(len(a)):
            if a[i] != b[i]:
                possible = False
                break
        
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()