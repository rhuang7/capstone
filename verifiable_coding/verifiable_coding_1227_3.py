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
        # Adjacent sides are:
        # front with left, right, top, bottom
        # back with left, right, top, bottom
        # left with front, back, top, bottom
        # right with front, back, top, bottom
        # top with front, back, left, right
        # bottom with front, back, left, right
        # Check all combinations of three adjacent sides
        # Check front, left, top
        if front == left == top:
            print("YES")
            continue
        # Check front, left, bottom
        if front == left == bottom:
            print("YES")
            continue
        # Check front, right, top
        if front == right == top:
            print("YES")
            continue
        # Check front, right, bottom
        if front == right == bottom:
            print("YES")
            continue
        # Check back, left, top
        if back == left == top:
            print("YES")
            continue
        # Check back, left, bottom
        if back == left == bottom:
            print("YES")
            continue
        # Check back, right, top
        if back == right == top:
            print("YES")
            continue
        # Check back, right, bottom
        if back == right == bottom:
            print("YES")
            continue
        # Check left, top, bottom
        if left == top == bottom:
            print("YES")
            continue
        # Check right, top, bottom
        if right == top == bottom:
            print("YES")
            continue
        # Check front, back, left
        if front == back == left:
            print("YES")
            continue
        # Check front, back, right
        if front == back == right:
            print("YES")
            continue
        # Check front, top, bottom
        if front == top == bottom:
            print("YES")
            continue
        # Check back, top, bottom
        if back == top == bottom:
            print("YES")
            continue
        # Check left, right, top
        if left == right == top:
            print("YES")
            continue
        # Check left, right, bottom
        if left == right == bottom:
            print("YES")
            continue
        # Check top, bottom, left
        if top == bottom == left:
            print("YES")
            continue
        # Check top, bottom, right
        if top == bottom == right:
            print("YES")
            continue
        print("NO")

if __name__ == '__main__':
    solve()