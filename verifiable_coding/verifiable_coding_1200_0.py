import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = input[1:T+1]

    for s in cases:
        count_a = s.count('A')
        count_b = s.count('B')
        if count_a != count_b:
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