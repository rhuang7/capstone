import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    strings = data[1:T+1]
    
    for s in strings:
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        count += 1
                    else:
                        mid = j - 1
                        if all(c == s[i] for c in s[i+1:mid]):
                            count += 1
        print(count)

if __name__ == '__main__':
    solve()