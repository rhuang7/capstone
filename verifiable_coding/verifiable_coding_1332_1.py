import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    idx = 1
    for _ in range(N):
        i = int(data[idx])
        j = int(data[idx+1])
        idx += 2
        # Find the length of the shortest path between i and j
        # The path is the number of steps to move up to the lowest common ancestor (LCA)
        # and then down to the other node
        # So we find the LCA by moving the deeper node up until both are at the same depth
        # Then move both up until they meet
        # Alternatively, we can find the number of steps to move both nodes up to their LCA
        # and sum those steps
        # Let's find the LCA by moving the deeper node up
        a, b = i, j
        depth_a = 0
        while a > 1:
            a //= 2
            depth_a += 1
        depth_b = 0
        while b > 1:
            b //= 2
            depth_b += 1
        # Bring the deeper node up to the same depth
        if depth_a > depth_b:
            a = i
            b = j
            for _ in range(depth_a - depth_b):
                a //= 2
        else:
            a = j
            b = i
            for _ in range(depth_b - depth_a):
                b //= 2
        # Now find the LCA
        steps = 0
        while a != b:
            a //= 2
            b //= 2
            steps += 1
        # The total steps is twice the steps to reach LCA from one node
        print(steps * 2)

if __name__ == '__main__':
    solve()