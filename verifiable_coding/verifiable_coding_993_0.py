import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:N+1]))
    
    for ai in a:
        if ai < 2:
            print("NO")
            continue
        # The first and last slots are occupied, so there are (ai - 2) empty slots
        # We need exactly one empty slot that divides ai
        # So, we need (ai - 2) to be exactly 1, and that slot must divide ai
        # Or, there must be exactly one divisor of ai (other than 1 and ai) which is (ai - 2)
        # So, check if (ai - 2) is a divisor of ai and (ai - 2) == 1
        if ai - 2 == 1:
            print("YES")
        else:
            # Check if (ai - 2) is a divisor of ai
            if ai % (ai - 2) == 0:
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    solve()