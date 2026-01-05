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
        # For each singer, find how many others are contained within it
        # A singer i is better than singer j if L_i <= L_j and U_i >= U_j
        # So we can use a binary search approach
        # Precompute for each singer, the number of singers that are contained within it
        scores = [0] * N
        for i in range(N):
            L_i, U_i = singers[i]
            # Find the number of singers j where L_j >= L_i and U_j <= U_i
            # Since singers are sorted, we can use binary search
            # Find the first singer with L_j >= L_i
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                if singers[mid][0] >= L_i:
                    right = mid
                else:
                    left = mid + 1
            # Now find the first singer with U_j > U_i
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                if singers[mid][1] > U_i:
                    right = mid
                else:
                    left = mid + 1
            count = left
            scores[i] = count * 2
        # Now for each pair (i, j), if i is better than j, then i gets 2 points, j gets 0
        # If j is better than i, then j gets 2 points, i gets 0
        # If neither is better than the other, both get 1 point
        # So we can compute the total points as:
        # For each i, the number of singers j where i is better than j is count_i
        # The number of singers j where j is better than i is count_j
        # The number of singers j where neither is better than the other is N - 1 - count_i - count_j
        # So total points for i is count_i * 2 + (N - 1 - count_i - count_j) * 1
        # But we need to compute count_j for each i
        # So we can precompute for each singer, the number of singers that are better than it
        # To do this, we can reverse the logic
        # For each singer i, find the number of singers j where L_j <= L_i and U_j >= U_i
        # So we can do the same binary search approach but in reverse
        # Precompute for each singer, the number of singers that are better than it
        better = [0] * N
        for i in range(N):
            L_i, U_i = singers[i]
            # Find the number of singers j where L_j <= L_i and U_j >= U_i
            # Since singers are sorted, we can use binary search
            # Find the first singer with L_j > L_i
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                if singers[mid][0] > L_i:
                    right = mid
                else:
                    left = mid + 1
            # Now find the first singer with U_j < U_i
            left = 0
            right = N
            while left < right:
                mid = (left + right) // 2
                if singers[mid][1] < U_i:
                    right = mid
                else:
                    left = mid + 1
            count = left
            better[i] = count
        # Now compute the total points for each singer
        for i in range(N):
            count_i = scores[i] // 2
            count_j = better[i]
            # The number of singers that are better than i is count_j
            # The number of singers that are contained in i is count_i
            # The number of singers that are neither is N - 1 - count_i - count_j
            # So total points is count_i * 2 + (N - 1 - count_i - count_j) * 1
            # But we need to make sure that count_i and count_j are not overlapping
            # So the total points is:
            total = count_i * 2 + (N - 1 - count_i - count_j) * 1
            scores[i] = total
        results.append(' '.join(map(str, scores)))
    print('\n'.join(results))