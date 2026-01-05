import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        required = {'L': 2, 'T': 2, 'I': 2, 'M': 2, 'E': 2}
        for key in required:
            if count.get(key, 0) < required[key]:
                print("NO")
                break
        else:
            print("YES")
            
if __name__ == '__main__':
    solve()