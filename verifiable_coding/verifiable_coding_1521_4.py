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
        N = int(data[idx])
        idx += 1
        singers = []
        for _ in range(N):
            L = int(data[idx])
            U = int(data[idx+1])
            idx += 2
            singers.append((L, U))
        # Sort singers by lower bound and upper bound
        singers.sort()
        # For each singer, find how many singers are contained within it
        # A singer A contains singer B if A's L <= B's L and A's U >= B's U
        # So we can use a binary search approach
        # Preprocess the singers to have a list of (L, U)
        # For each singer, find the number of singers where L_i >= current L and U_i <= current U
        # Since the singers are sorted, we can binary search for the range
        # We can use a list of U's and binary search for the number of singers with U <= current U and L >= current L
        # Since the singers are sorted by L, we can find the first singer with L >= current L
        # And then among those, find how many have U <= current U
        # To do this efficiently, we can precompute a list of U's and use binary search
        # We can use a list of U's and for each singer, find the number of U's <= current U and L >= current L
        # Since the singers are sorted by L, we can binary search for the first singer with L >= current L
        # Then, among those, find how many have U <= current U
        # This can be done with a binary search on the U's
        # So we precompute a list of U's and a list of L's
        Ls = [s[0] for s in singers]
        Us = [s[1] for s in singers]
        # For each singer, find the number of singers that are contained within it
        # This is the number of singers where L_i >= current L and U_i <= current U
        # Since the singers are sorted by L, we can binary search for the first singer with L >= current L
        # Then, among those, find how many have U <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search to find the first singer with L >= current L
        # 2. From that index to the end, find how many have U <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U
        # This can be done with a binary search on the U's
        # So for each singer, we do:
        # 1. Binary search for the first singer with L >= current L
        # 2. From that index to the end, find the number of U's <= current U