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
                start = depth_stack.pop()
                current_depth = depth
                if current_depth > max_depth:
                    max_depth = current_depth
                    first_depth_pos = start
                # Calculate the length of the bracket pair
                length = i + 1 - start + 1
                # Track the maximum length and its first occurrence
                if length > max_depth:
                    max_depth = length
                    first_depth_pos = start
                elif length == max_depth:
                    if first_depth_pos == 0 or start < first_depth_pos:
                        first_depth_pos = start

    # Now find the first occurrence of the max_depth in the depth stack
    # We need to find the first position where the depth is max_depth
    # We'll do a second pass to find the first occurrence of max_depth
    first_depth_pos = 0
    for i in range(N):
        if brackets[i] == 1:
            depth += 1
            if depth == max_depth:
                first_depth_pos = i + 1
                break
        else:
            if depth_stack:
                start = depth_stack.pop()
                if depth == max_depth:
                    first_depth_pos = start
                    break

    print(f"{max_depth} {first_depth_pos} {max_depth} {first_depth_pos}")

if __name__ == '__main__':
    solve()