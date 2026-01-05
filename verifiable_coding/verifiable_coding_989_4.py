import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index+1])
        K = int(data[index+2])
        index += 3
        total = X + Y
        served = 0
        # Determine how many times the server has changed
        # Each time K points are scored, the server changes
        # So the number of server changes is total // K
        # The initial server is Chef
        # If the number of server changes is even, Chef serves next
        # If odd, Paja serves next
        if (total // K) % 2 == 0:
            print("Chef")
        else:
            print("Paja")

if __name__ == '__main__':
    solve()