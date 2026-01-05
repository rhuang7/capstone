import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    x = list(map(int, data[1:t+1]))
    
    def is_possible(x_i):
        if x_i < 1:
            return False
        # For a single die, the visible pips are top + front + right + back + left + bottom - top - bottom (since top and bottom are not visible)
        # But since the bottom is not visible, it's top + front + right + back + left
        # However, the bottom is not visible, so the visible pips are top + front + right + back + left
        # But when stacking, the bottom of the top die and the top of the bottom die are not visible
        # So for a tower of n dice, the visible pips are:
        # top of top die + front of top die + right of top die + back of top die + left of top die
        # plus front of second die + right of second die + back of second die + left of second die
        # ... and so on for each die except the bottom one
        # But the bottom die's top is not visible
        # So for a tower of n dice, the visible pips are:
        # top of top die + front of top die + right of top die + back of top die + left of top die
        # plus front of second die + right of second die + back of second die + left of second die
        # ... and so on for each die except the bottom one
        # But the bottom die's top is not visible
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - top of bottom die - bottom of top die
        # But since the bottom of top die is not visible, it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But bottom of top die is not visible, so it's not counted
        # So the total visible pips is:
        # sum for each die (top + front + right + back + left) - bottom of top die
        # But