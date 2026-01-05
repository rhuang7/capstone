import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    brackets = list(map(int, data[1:]))

    depth = 0
    max_depth = 0
    first_depth_pos = 0

    depth_stack = []
    for i in range(N):
        if brackets[i] == 1:
            depth += 1
            depth_stack.append(i + 1)  # positions are 1-based
            if depth > max_depth:
                max_depth = depth
                first_depth_pos = i + 1
        else:
            if depth_stack:
                start_pos = depth_stack.pop()
                current_depth = depth
                if current_depth > max_depth:
                    max_depth = current_depth
                    first_depth_pos = start_pos
                # Calculate length of bracket pair
                length = i + 1 - start_pos + 1
                if length > max_len:
                    max_len = length
                    first_max_pos = start_pos

    print(f"{max_depth} {first_depth_pos} {max_len} {first_max_pos}")

if __name__ == '__main__':
    solve()