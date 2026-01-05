import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        colors = input[idx:idx+6]
        idx += 6
        front, back, left, right, top, bottom = colors
        # Check all combinations of three sides that are pairwise adjacent
        # Adjacent pairs are:
        # (front, left), (front, right), (front, top), (front, bottom)
        # (back, left), (back, right), (back, top), (back, bottom)
        # (left, top), (left, bottom)
        # (right, top), (right, bottom)
        # (top, bottom)
        # We need three sides that are pairwise adjacent, which means they share a common vertex
        # So check all combinations of three sides that share a common vertex
        # The cube has 8 vertices, each with 3 adjacent sides
        # We can check all possible triplets of sides that share a common vertex
        # The valid triplets are:
        # (front, left, top)
        # (front, left, bottom)
        # (front, right, top)
        # (front, right, bottom)
        # (back, left, top)
        # (back, left, bottom)
        # (back, right, top)
        # (back, right, bottom)
        # (left, top, bottom)
        # (right, top, bottom)
        # (top, front, left)
        # (top, front, right)
        # (top, back, left)
        # (top, back, right)
        # (bottom, front, left)
        # (bottom, front, right)
        # (bottom, back, left)
        # (bottom, back, right)
        # (front, left, right)
        # (front, top, bottom)
        # (back, left, right)
        # (back, top, bottom)
        # (left, top, right)
        # (left, bottom, right)
        # (top, left, right)
        # (bottom, left, right)
        # (front, left, top)
        # (front, left, bottom)
        # (front, right, top)
        # (front, right, bottom)
        # (back, left, top)
        # (back, left, bottom)
        # (back, right, top)
        # (back, right, bottom)
        # (left, top, bottom)
        # (right, top, bottom)
        # (top, front, left)
        # (top, front, right)
        # (top, back, left)
        # (top, back, right)
        # (bottom, front, left)
        # (bottom, front, right)
        # (bottom, back, left)
        # (bottom, back, right)
        # (front, left, right)
        # (front, top, bottom)
        # (back, left, right)
        # (back, top, bottom)
        # (left, top, right)
        # (left, bottom, right)
        # (top, left, right)
        # (bottom, left, right)
        # Check all possible triplets
        # We can check all possible triplets of sides
        # There are C(6,3) = 20 possible triplets
        # For each triplet, check if all three are the same color and are pairwise adjacent
        # We can predefine all valid triplets of adjacent sides
        valid_triplets = [
            (front, left, top),
            (front, left, bottom),
            (front, right, top),
            (front, right, bottom),
            (back, left, top),
            (back, left, bottom),
            (back, right, top),
            (back, right, bottom),
            (left, top, bottom),
            (right, top, bottom),
            (top, front, left),
            (top, front, right),
            (top, back, left),
            (top, back, right),
            (bottom, front, left),
            (bottom, front, right),
            (bottom, back, left),
            (bottom, back, right),
            (front, left, right),
            (front, top, bottom),
            (back, left, right),
            (back, top, bottom),
            (left, top, right),
            (left, bottom, right),
            (top, left, right),
            (bottom, left, right)
        ]
        found = False
        for triplet in valid_triplets:
            if triplet[0] == triplet[1] == triplet[2]:
                found = True
                break
        print("YES" if found else "NO")

if __name__ == '__main__':
    solve()