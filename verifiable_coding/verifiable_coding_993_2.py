import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    
    for ai in a:
        if ai <= 2:
            print("NO")
            continue
        # The first and last slots are occupied, so there are (ai - 2) empty slots
        # We need exactly one empty slot that divides ai
        # So we need (ai - 2) == 1 and ai is divisible by 1 (which it always is)
        # Or (ai - 2) is a number that has exactly one divisor (which is itself)
        # Which means (ai - 2) must be 1
        if ai - 2 == 1:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()