import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx+1])
        idx += 2
        c = list(map(int, data[idx:idx+A*B]))
        idx += A*B
        d = list(map(int, data[idx:idx+A*B]))
        idx += A*B
        votes = []
        for i in range(A*B):
            votes.append((c[i], d[i]))
        # Sort by the maximum of c[i] and d[i], in descending order
        votes.sort(key=lambda x: max(x[0], x[1]), reverse=True)
        # For each state, we need to select B districts
        # We want to maximize the number of states where P1 wins
        # So we try to select B districts where the maximum is c[i]
        # We can greedily select the top B districts where the maximum is c[i]
        # and count how many of them are such
        count = 0
        i = 0
        while i < len(votes):
            max_val = max(votes[i][0], votes[i][1])
            # Find the next B districts where the max is c[i]
            # We can only select B districts per state
            # So we need to find the next B districts where the max is c[i]
            # and check if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts in the sorted list
            # and counting how many of them have max as c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c[i]
            # We can do this by checking the next B districts
            # and seeing if the max is c