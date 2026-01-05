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
                else:
                    if current_depth == max_depth and first_depth_pos == 0:
                        first_depth_pos = start_pos
    
    # Now find the maximum length between matching brackets
    max_length = 0
    first_max_pos = 0
    stack = []
    for i in range(N):
        if brackets[i] == 1:
            stack.append(i + 1)
        else:
            if stack:
                start = stack.pop()
                length = i + 1 - start + 1
                if length > max_length:
                    max_length = length
                    first_max_pos = start
                elif length == max_length and first_max_pos == 0:
                    first_max_pos = start
    
    print(f"{max_depth} {first_depth_pos} {max_length} {first_max_pos}")

if __name__ == '__main__':
    solve()