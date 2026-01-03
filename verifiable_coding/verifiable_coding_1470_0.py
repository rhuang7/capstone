import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        count += 1
                    else:
                        valid = True
                        for k in range(i+1, j):
                            if s[k] != s[i+1]:
                                valid = False
                                break
                        if valid:
                            count += 1
        print(count)

if __name__ == '__main__':
    solve()