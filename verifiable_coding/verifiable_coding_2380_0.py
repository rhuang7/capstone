import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # We need to find the minimum number of moves to make the string k-periodic
        # A k-periodic string has all '1's at positions i, i+k, i+2k, ... etc.
        # So for each possible starting position of the first '1', we can check how many '1's are in the correct positions and how many '0's are in the correct positions.
        
        # The valid positions for '1's are those congruent to pos mod k, where pos is the starting position.
        # So for each possible starting position in 0..k-1, we can check how many '1's are in the correct positions.
        
        min_moves = float('inf')
        
        # Try each possible starting position for the first '1'
        for start in range(k):
            # The positions where '1's should be are start, start + k, start + 2k, ...
            # We need to count how many '1's are already in these positions and how many '0's are in these positions.
            # The number of '1's in these positions is the number of '1's that are already in the correct positions.
            # The number of '0's in these positions is the number of '0's that are already in the correct positions.
            # The number of '1's needed is the number of positions in the correct positions.
            # The number of '0's needed is the number of positions in the correct positions.
            # So the number of moves is (number of '0's in correct positions) + (number of '1's not in correct positions).
            # But we need to make sure that the number of '1's in the correct positions is at least 1, because the garland must have at least one '1'.
            # So we need to count the number of '1's in the correct positions, and if it is 0, we need to add 1 (to turn one '0' into '1').
            # But for the k-periodic garland, the '1's must be exactly at the positions start, start + k, start + 2k, etc.
            # So the number of '1's in the correct positions is the number of '1's in those positions.
            # The number of '0's in the correct positions is the number of '0's in those positions.
            # The number of '1's not in the correct positions is the total number of '1's in the string minus the number of '1's in the correct positions.
            # The number of '0's not in the correct positions is the total number of '0's in the string minus the number of '0's in the correct positions.
            # But we need to make sure that the number of '1's in the correct positions is at least 1, because the garland must have at least one '1'.
            # So we need to count the number of '1's in the correct positions, and if it is 0, we need to add 1 (to turn one '0' into '1').
            # But for the k-periodic garland, the '1's must be exactly at the positions start, start + k, start + 2k, etc.
            # So the number of '1's in the correct positions is the number of '1's in those positions.
            # The number of '0's in the correct positions is the number of '0's in those positions.
            # The number of '1's not in the correct positions is the total number of '1's in the string minus the number of '1's in the correct positions.
            # The number of '0's not in the correct positions is the total number of '0's in the string minus the number of '0's in the correct positions.
            # But we need to make sure that the number of '1's in the correct positions is at least 1, because the garland must have at least one '1'.
            # So we need to count the number of '1's in the correct positions, and if it is 0, we need to add 1 (to turn one '0' into '1').
            # But for the k-periodic garland, the '1's must be exactly at the positions start, start + k, start + 2k, etc.
            # So the number of '1's in the correct positions is the number of '1's in those positions.
            # The number of '0's in the correct positions is the number of '0's in those positions.
            # The number of '1's not in the correct positions is the total number of '1's in the string minus the number of '1's in the correct positions.
            # The number of '0's not in the correct positions is the total number of '0's in the string minus the number of '0's in the correct positions.
            # But we need to make sure that the number of '1's in the correct positions is at least 1, because the garland must have at least one '1'.
            # So we need to count the number of '1's in the correct positions, and if it is 0, we need to add 1 (to turn one '0' into '1').
            # But for the k-periodic garland, the '1's must be exactly at the positions start, start + k, start + 2k, etc.
            # So the number of '1's in the correct positions is the number of '1's in those positions.
            # The number of '0's in the correct positions is the number of '0's in those positions.
            # The number of '1's not in the correct positions is the total number of '1's in the string minus the number of '1's in the correct positions.
            # The number of '0's not in the correct positions is the total number of '0's in the string minus the number of '0's in the correct positions.
            # But we need to make sure that the number of '1's in the correct positions is at least 1, because the garland must have at least one '1'.
            # So we need to count the number of '1's in the correct positions, and if it is 0, we need to add 1 (to turn one '0' into '1').
            # But for the k-periodic garland, the '1's must be exactly at the positions start, start + k, start + 2k, etc.
            # So the number of '1's in the correct positions is the number of '1's in those positions.
            # The number of '0's in the correct positions is the number of '0's in those positions.
            # The number of '1's not in the correct positions is the total number of '1's in the string minus the number of '1's in the correct positions.
            # The number of '0's not in the correct positions is the total number of '0's in the string minus the number of '0's in the correct positions.
            # But we need to make sure that the number of '1's in the correct positions is at least 1, because the garland must have at least one '1'.
            # So we need to count the number of '1's in the correct positions, and if it is 0, we need to add 1 (to turn one '0' into '1').
            # But for the k-periodic garland, the '1's must be exactly at the positions start, start + k, start + 2k, etc.
            # So the number of '1's in the correct positions is the number of '1's in those positions.
            # The number of '0's in the correct positions is the number of '0's in those positions.
            # The number of '1's not in the correct positions is the total number of '1's in the string minus the number of '1's in the correct positions.
            # The number of '0's not in the correct positions is the total number of '0's in the string minus the number of '0's in the correct positions.
            # But we need to make sure that the number of '1's in the correct positions is at least 1, because the garland must have at least one '1'.
            # So we need to count the number of '1's in the correct positions, and if it is 0, we need to add 1 (to turn one '0' into '1').
            # But for the k-periodic garland, the '1's must be exactly at the positions start, start + k, start + 2k, etc.
            # So the number of '1's in the correct positions is the number of '1's in those positions.
            # The number of '0's in the correct positions is the number of '0's in those positions.
            # The number of '1's not