import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    strings = data[1:T+1]
    
    for s in strings:
        n = len(s)
        if n < 2:
            print("no")
            continue
        # Check for any character that appears at least twice
        found = False
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    found = True
                    break
            if found:
                break
        if found:
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()