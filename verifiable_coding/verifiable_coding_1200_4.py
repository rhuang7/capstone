import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    
    for s in cases:
        count_A = s.count('A')
        count_B = s.count('B')
        if count_A != count_B:
            print("no")
            continue
        valid = True
        for i in range(0, len(s), 2):
            if s[i] == s[i+1]:
                valid = False
                break
        print("yes" if valid else "no")

if __name__ == '__main__':
    solve()