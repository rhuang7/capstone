import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        if N == 1:
            results.append("-1")
            continue
        
        # Initial state: top=1, front=2, right=3, bottom=4, back=5, left=6
        # But we need to find the correct initial state based on the sequence
        # Try all possible initial states (6 possibilities)
        # Each die state can be represented as a tuple (top, front, right)
        # Opposite faces are: top -> bottom, front -> back, right -> left
        # So for a die state (top, front, right), the opposite faces are:
        # o(top) = bottom, o(front) = back, o(right) = left
        # And the bottom is 7 - top, back is 7 - front, left is 7 - right
        
        # Try all possible initial states
        possible = []
        for top in range(1, 7):
            for front in range(1, 7):
                if front == top:
                    continue
                for right in range(1, 7):
                    if right == top or right == front:
                        continue
                    # Check if this initial state can produce the sequence A
                    current_top = top
                    current_front = front
                    current_right = right
                    valid = True
                    for i in range(N-1):
                        # Roll the die in one of the 4 directions
                        # We need to determine the direction based on the next value in A
                        # The next value is the new top
                        next_top = A[i+1]
                        # Find the direction that would make next_top the new top
                        # Possible directions:
                        # 1. Roll forward: new top = front, new front = bottom (7 - top), new bottom = back (7 - front), new back = top
                        # 2. Roll backward: new top = back, new back = top, new bottom = front, new front = 7 - top
                        # 3. Roll right: new top = right, new right = top, new bottom = left, new left = 7 - top
                        # 4. Roll left: new top = left, new left = top, new bottom = right, new right = 7 - top
                        # Try all 4 directions
                        # Check if any direction leads to next_top
                        # Check direction 1: roll forward
                        new_top1 = front
                        new_front1 = 7 - top
                        new_bottom1 = 7 - front
                        new_back1 = top
                        if new_top1 == next_top:
                            current_top, current_front, current_right = new_top1, new_front1, current_right
                            continue
                        # Check direction 2: roll backward
                        new_top2 = 7 - front
                        new_back2 = front
                        new_bottom2 = front
                        new_front2 = 7 - top
                        if new_top2 == next_top:
                            current_top, current_front, current_right = new_top2, new_back2, current_right
                            continue
                        # Check direction 3: roll right
                        new_top3 = right
                        new_right3 = top
                        new_bottom3 = 7 - right
                        new_left3 = top
                        if new_top3 == next_top:
                            current_top, current_front, current_right = new_top3, current_front, new_right3
                            continue
                        # Check direction 4: roll left
                        new_top4 = 7 - right
                        new_left4 = top
                        new_bottom4 = right
                        new_right4 = 7 - top
                        if new_top4 == next_top:
                            current_top, current_front, current_right = new_top4, current_front, new_left4
                            continue
                        # If none of the directions work, this initial state is invalid
                        valid = False
                        break
                    if valid:
                        # Calculate the opposite faces
                        bottom = 7 - current_top
                        back = 7 - current_front
                        left = 7 - current_right
                        # Opposite faces:
                        # o(top) = bottom
                        # o(front) = back
                        # o(right) = left
                        # So we need to map the numbers 1-6 to their opposite faces
                        # Create a dictionary that maps each number to its opposite
                        # First, find which number is top, front, right, bottom, back, left
                        # Then, for each number 1-6, find its opposite
                        # We can do this by checking which of the six numbers is top, front, right, bottom, back, left
                        # So create a list of the six numbers: top, front, right, bottom, back, left
                        # Then, for each number in 1-6, find its opposite
                        # The opposite of top is bottom, front is back, right is left
                        # So the list is [top, front, right, bottom, back, left]
                        # The opposite of each number is the one at the opposite index
                        # So for index 0 (top), opposite is index 3 (bottom)
                        # For index 1 (front), opposite is index 4 (back)
                        # For index 2 (right), opposite is index 5 (left)
                        # So the opposite of each number is:
                        # o(top) = bottom
                        # o(front) = back
                        # o(right) = left
                        # So create a list of the six numbers in order: top, front, right, bottom, back, left
                        # Then, for each number in 1-6, find its opposite
                        # So create a dictionary: for each number, find its index in the list, then find the opposite index
                        # Then, the opposite is the number at that index
                        # So create the list
                        die = [current_top, current_front, current_right, bottom, back, left]
                        # Create a dictionary that maps each number to its opposite
                        opposite = {}
                        for i in range(6):
                            opposite[die[i]] = die[3 - i]
                        # Now, for each number from 1 to 6, output its opposite
                        # So the output is opposite[1], opposite[2], opposite[3], opposite[4], opposite[5], opposite[6]
                        # But wait, the problem says to output o(1), o(2), ..., o(6)
                        # So the output is the opposite of 1, 2, 3, 4, 5, 6
                        output = [opposite[i] for i in range(1, 7)]
                        possible.append(output)
        
        if len(possible) == 0:
            results.append("-1")
        else:
            results.append(" ".join(map(str, possible[0])))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()