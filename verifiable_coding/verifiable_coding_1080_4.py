import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for s in cases:
        if len(s) < 2:
            print("NO")
            continue
        first = s[0]
        second = s[1]
        if first == second:
            print("NO")
            continue
        is_alternating = True
        for i in range(2, len(s)):
            if (i % 2 == 0 and s[i] == first) or (i % 2 == 1 and s[i] == second):
                continue
            else:
                is_alternating = False
                break
        print("YES" if is_alternating else "NO")

if __name__ == '__main__':
    solve()