import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        # Convert the string to a list of characters
        s_list = list(s)
        # Group consecutive characters
        groups = []
        i = 0
        while i < len(s_list):
            current = s_list[i]
            j = i
            while j < len(s_list) and s_list[j] == current:
                j += 1
            groups.append((current, j - i))
            i = j
        
        # Calculate the total number of 1's
        total_ones = sum(count for char, count in groups if char == '1')
        # The game is played optimally, so the players take turns taking the maximum possible 1's
        # The first player (Alice) will take the maximum possible 1's on her turn
        # The second player (Bob) will take the maximum possible 1's on his turn
        # This is a game of taking turns, so the result is total_ones // 2 if total_ones is even, else (total_ones + 1) // 2
        alice_score = total_ones // 2 if total_ones % 2 == 0 else (total_ones + 1) // 2
        print(alice_score)

if __name__ == '__main__':
    solve()