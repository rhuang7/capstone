import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        colors = input[idx:idx+6]
        idx += 6
        front, back, left, right, top, bottom = colors
        # Check all possible triplets of adjacent sides
        # Adjacent sides are: front with left, right, top, bottom
        # back with left, right, top, bottom
        # left with front, back, top, bottom
        # right with front, back, top, bottom
        # top with front, back, left, right
        # bottom with front, back, left, right
        # Check all combinations of three adjacent sides
        # We can check all possible triplets of adjacent sides
        # There are 12 possible triplets of adjacent sides
        # For each triplet, check if all three have the same color
        # Check all possible triplets of adjacent sides
        # Front, left, top
        if front == left == top:
            print("YES")
            continue
        # Front, left, bottom
        if front == left == bottom:
            print("YES")
            continue
        # Front, right, top
        if front == right == top:
            print("YES")
            continue
        # Front, right, bottom
        if front == right == bottom:
            print("YES")
            continue
        # Back, left, top
        if back == left == top:
            print("YES")
            continue
        # Back, left, bottom
        if back == left == bottom:
            print("YES")
            continue
        # Back, right, top
        if back == right == top:
            print("YES")
            continue
        # Back, right, bottom
        if back == right == bottom:
            print("YES")
            continue
        # Left, top, bottom
        if left == top == bottom:
            print("YES")
            continue
        # Right, top, bottom
        if right == top == bottom:
            print("YES")
            continue
        # Left, front, top
        if left == front == top:
            print("YES")
            continue
        # Right, front, top
        if right == front == top:
            print("YES")
            continue
        # Left, back, top
        if left == back == top:
            print("YES")
            continue
        # Right, back, top
        if right == back == top:
            print("YES")
            continue
        # Left, front, bottom
        if left == front == bottom:
            print("YES")
            continue
        # Right, front, bottom
        if right == front == bottom:
            print("YES")
            continue
        # Left, back, bottom
        if left == back == bottom:
            print("YES")
            continue
        # Right, back, bottom
        if right == back == bottom:
            print("YES")
            continue
        # Top, front, left
        if top == front == left:
            print("YES")
            continue
        # Top, front, right
        if top == front == right:
            print("YES")
            continue
        # Top, back, left
        if top == back == left:
            print("YES")
            continue
        # Top, back, right
        if top == back == right:
            print("YES")
            continue
        # Bottom, front, left
        if bottom == front == left:
            print("YES")
            continue
        # Bottom, front, right
        if bottom == front == right:
            print("YES")
            continue
        # Bottom, back, left
        if bottom == back == left:
            print("YES")
            continue
        # Bottom, back, right
        if bottom == back == right:
            print("YES")
            continue
        print("NO")

if __name__ == '__main__':
    solve()