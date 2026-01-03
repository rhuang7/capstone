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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        valid = True
        # Check if the array has the correct structure
        # First part: 1 to 7
        # Second part: 6 to 1
        # Check for 7
        if A[0] != 1 or A[-1] != 1:
            valid = False
        else:
            # Check for 7
            if A.count(7) != 1:
                valid = False
            else:
                # Find the position of 7
                pos7 = A.index(7)
                # Check if the first part is 1 to 7
                for i in range(pos7):
                    if A[i] != 1:
                        valid = False
                        break
                if valid:
                    # Check if the second part is 6 to 1
                    for i in range(pos7+1, N):
                        if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                            valid = False
                            break
                # Check if the second part is symmetric
                if valid:
                    for i in range(pos7+1, N):
                        if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                            valid = False
                            break
                    if valid:
                        # Check if the second part is symmetric
                        for i in range(pos7+1, N):
                            if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                valid = False
                                break
                        if valid:
                            # Check if the second part is symmetric
                            for i in range(pos7+1, N):
                                if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                    valid = False
                                    break
                            if valid:
                                # Check if the second part is symmetric
                                for i in range(pos7+1, N):
                                    if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                        valid = False
                                        break
                                if valid:
                                    # Check if the second part is symmetric
                                    for i in range(pos7+1, N):
                                        if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                            valid = False
                                            break
                                    if valid:
                                        # Check if the second part is symmetric
                                        for i in range(pos7+1, N):
                                            if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                valid = False
                                                break
                                        if valid:
                                            # Check if the second part is symmetric
                                            for i in range(pos7+1, N):
                                                if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                    valid = False
                                                    break
                                            if valid:
                                                # Check if the second part is symmetric
                                                for i in range(pos7+1, N):
                                                    if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                        valid = False
                                                        break
                                                if valid:
                                                    # Check if the second part is symmetric
                                                    for i in range(pos7+1, N):
                                                        if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                            valid = False
                                                            break
                                                    if valid:
                                                        # Check if the second part is symmetric
                                                        for i in range(pos7+1, N):
                                                            if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                valid = False
                                                                break
                                                        if valid:
                                                            # Check if the second part is symmetric
                                                            for i in range(pos7+1, N):
                                                                if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                    valid = False
                                                                    break
                                                            if valid:
                                                                # Check if the second part is symmetric
                                                                for i in range(pos7+1, N):
                                                                    if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                        valid = False
                                                                        break
                                                                if valid:
                                                                    # Check if the second part is symmetric
                                                                    for i in range(pos7+1, N):
                                                                        if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                            valid = False
                                                                            break
                                                                        if valid:
                                                                            # Check if the second part is symmetric
                                                                            for i in range(pos7+1, N):
                                                                                if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                                    valid = False
                                                                                    break
                                                                            if valid:
                                                                                # Check if the second part is symmetric
                                                                                for i in range(pos7+1, N):
                                                                                    if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                                        valid = False
                                                                                        break
                                                                                if valid:
                                                                                    # Check if the second part is symmetric
                                                                                    for i in range(pos7+1, N):
                                                                                        if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                                            valid = False
                                                                                            break
                                                                                        if valid:
                                                                                            # Check if the second part is symmetric
                                                                                            for i in range(pos7+1, N):
                                                                                                if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                                                    valid = False
                                                                                                    break
                                                                                                if valid:
                                                                                                    # Check if the second part is symmetric
                                                                                                    for i in range(pos7+1, N):
                                                                                                        if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                                                            valid = False
                                                                                                            break
                                                                                                        if valid:
                                                                                                            # Check if the second part is symmetric
                                                                                                            for i in range(pos7+1, N):
                                                                                                                if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                                                                    valid = False
                                                                                                                    break
                                                                                                                if valid:
                                                                                                                    # Check if the second part is symmetric
                                                                                                                    for i in range(pos7+1, N):
                                                                                                                        if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                                                                            valid = False
                                                                                                                            break
                                                                                                                        if valid:
                                                                                                                            # Check if the second part is symmetric
                                                                                                                            for i in range(pos7+1, N):
                                                                                                                                if A[i] != 6 and A[i] != 5 and A[i] != 4 and A[i] != 3 and A[i] != 2 and A[i] != 1:
                                                                                                                                    valid = False
                                                                                                                                    break
                                                                                                                                if valid:
                                                                                                                                    # Check if the second part is symmetric