import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        x = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        for __ in range(Q):
            query_type = int(data[idx])
            idx += 1
            if query_type == 1:
                i = int(data[idx])
                idx += 1
                if (x >> (i - 1)) & 1:
                    print("ON")
                else:
                    print("OFF")
            elif query_type == 2:
                i = int(data[idx])
                idx += 1
                x |= (1 << (i - 1))
            elif query_type == 3:
                i = int(data[idx])
                idx += 1
                x &= ~(1 << (i - 1))
            elif query_type == 4:
                p = int(data[idx])
                q = int(data[idx+1])
                idx += 2
                if (x >> (p - 1)) & 1:
                    x ^= (1 << (p - 1))
                if (x >> (q - 1)) & 1:
                    x ^= (1 << (q - 1))