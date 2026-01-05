import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        # Convert the string into a list of characters
        s_list = list(s)
        # Group consecutive equal characters
        groups = []
        i = 0
        while i < len(s_list):
            current = s_list[i]
            j = i
            while j < len(s_list) and s_list[j] == current:
                j += 1
            groups.append((current, j - i))
            i = j
        
        # Calculate the total number of 1s
        total_ones = sum(count for char, count in groups if char == '1')
        # The game is played optimally, so the total number of 1s is split between Alice and Bob
        # Alice goes first, so she gets the ceiling of total_ones / 2
        alice_score = (total_ones + 1) // 2
        print(alice_score)

if __name__ == '__main__':
    solve()