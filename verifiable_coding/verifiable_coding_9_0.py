import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        # Group consecutive characters
        groups = []
        prev = s[0]
        count = 1
        for c in s[1:]:
            if c == prev:
                count += 1
            else:
                groups.append((prev, count))
                prev = c
                count = 1
        groups.append((prev, count))
        
        # Calculate the total number of 1s
        total_ones = sum(c[1] for c in groups if c[0] == '1')
        
        # If there are no 1s, Alice's score is 0
        if total_ones == 0:
            print(0)
            continue
        
        # Simulate the game
        # We use a greedy approach: always take the largest group of 1s
        # and alternate between Alice and Bob
        alice = 0
        bob = 0
        i = 0
        while i < len(groups):
            if groups[i][0] == '1':
                # Take the largest group of 1s
                max_group = 0
                max_idx = i
                for j in range(i, len(groups)):
                    if groups[j][0] == '1' and groups[j][1] > max_group:
                        max_group = groups[j][1]
                        max_idx = j
                # Remove the max group
                alice += max_group if (i % 2 == 0) else bob
                bob += max_group if (i % 2 == 1) else alice
                # Remove the group from the list
                groups = groups[:max_idx] + groups[max_idx+1:]
                i = 0
            else:
                i += 1
        
        print(alice)

if __name__ == '__main__':
    solve()