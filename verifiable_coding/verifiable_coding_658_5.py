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
        n = int(data[idx])
        idx += 1
        s = list(map(int, data[idx:idx + n]))
        idx += n
        
        max_len = 0
        # Check the original sequence
        current_len = 1
        for i in range(1, n):
            if (i % 2 == 1 and s[i] >= s[i - 1]) or (i % 2 == 0 and s[i] <= s[i - 1]):
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)
        
        # Try inserting at each position
        for i in range(n + 1):
            # Try inserting a value that makes the sequence UpDown
            # Check the left and right parts
            left = []
            right = []
            if i > 0:
                left = s[:i]
            if i < n:
                right = s[i:]
            
            # Try to find a value to insert
            # Check the left and right parts for possible insertion
            # Check the left part
            left_len = 1
            for j in range(1, len(left)):
                if (j % 2 == 1 and left[j] >= left[j - 1]) or (j % 2 == 0 and left[j] <= left[j - 1]):
                    left_len += 1
                else:
                    left_len = 1
            # Check the right part
            right_len = 1
            for j in range(1, len(right)):
                if (j % 2 == 1 and right[j] >= right[j - 1]) or (j % 2 == 0 and right[j] <= right[j - 1]):
                    right_len += 1
                else:
                    right_len = 1
            
            # Check if the left and right can be merged
            # Check the left end and right end
            if i > 0 and i < n:
                # Check if the left end and right end can be connected
                # Check if the left end is <= the right end
                if left[-1] <= right[0]:
                    # Check if the left and right can be merged
                    # Check the left part and right part
                    # Check the left part
                    left_len = 1
                    for j in range(1, len(left)):
                        if (j % 2 == 1 and left[j] >= left[j - 1]) or (j % 2 == 0 and left[j] <= left[j - 1]):
                            left_len += 1
                        else:
                            left_len = 1
                    # Check the right part
                    right_len = 1
                    for j in range(1, len(right)):
                        if (j % 2 == 1 and right[j] >= right[j - 1]) or (j % 2 == 0 and right[j] <= right[j - 1]):
                            right_len += 1
                        else:
                            right_len = 1
                    # Check if the left and right can be merged
                    # Check the left end and right end
                    if left[-1] <= right[0]:
                        # Check the left and right parts
                        # Check the left part
                        left_len = 1
                        for j in range(1, len(left)):
                            if (j % 2 == 1 and left[j] >= left[j - 1]) or (j % 2 == 0 and left[j] <= left[j - 1]):
                                left_len += 1
                            else:
                                left_len = 1
                        # Check the right part
                        right_len = 1
                        for j in range(1, len(right)):
                            if (j % 2 == 1 and right[j] >= right[j - 1]) or (j % 2 == 0 and right[j] <= right[j - 1]):
                                right_len += 1
                            else:
                                right_len = 1
                        # Check if the left and right can be merged
                        # Check the left end and right end
                        if left[-1] <= right[0]:
                            # Check if the left and right parts can be merged
                            # Check the left part
                            left_len = 1
                            for j in range(1, len(left)):
                                if (j % 2 == 1 and left[j] >= left[j - 1]) or (j % 2 == 0 and left[j] <= left[j - 1]):
                                    left_len += 1
                                else:
                                    left_len = 1
                            # Check the right part
                            right_len = 1
                            for j in range(1, len(right)):
                                if (j % 2 == 1 and right[j] >= right[j - 1]) or (j % 2 == 0 and right[j] <= right[j - 1]):
                                    right_len += 1
                                else:
                                    right_len = 1
                            # Check if the left and right can be merged
                            # Check the left end and right end
                            if left[-1] <= right[0]:
                                # Check if the left and right parts can be merged
                                # Check the left part
                                left_len = 1
                                for j in range(1, len(left)):
                                    if (j % 2 == 1 and left[j] >= left[j - 1]) or (j % 2 == 0 and left[j] <= left[j - 1]):
                                        left_len += 1
                                    else:
                                        left_len = 1
                                # Check the right part
                                right_len = 1
                                for j in range(1, len(right)):
                                    if (j % 2 == 1 and right[j] >= right[j - 1]) or (j % 2 == 0 and right[j] <= right[j - 1]):
                                        right_len += 1
                                    else:
                                        right_len = 1
                                # Check if the left and right can be merged
                                # Check the left end and right end
                                if left[-1] <= right[0]:
                                    # Check if the left and right parts can be merged
                                    # Check the left part
                                    left_len = 1
                                    for j in range(1, len(left)):
                                        if (j % 2 == 1 and left[j] >= left[j - 1]) or (j % 2 == 0 and left[j] <= left[j - 1]):
                                            left_len += 1
                                        else:
                                            left_len = 1
                                    # Check the right part
                                    right_len = 1
                                    for j in range(1, len(right)):
                                        if (j % 2 == 1 and right[j] >= right[j - 1]) or (j % 2 == 0 and right[j] <= right[j - 1]):
                                            right_len += 1
                                        else:
                                            right_len = 1
                                    # Check if the left and right can be merged
                                    # Check the left end and right end
                                    if left[-1] <= right[0]:
                                        # Check if the left and right parts can be merged
                                        # Check the left part
                                        left_len = 1
                                        for j in range(1, len(left)):
                                            if (j % 2 == 1 and left[j] >= left[j - 1]) or (j % 2 == 0 and left[j] <= left[j - 1]):
                                                left_len += 1
                                            else:
                                                left_len = 1
                                        # Check the right part
                                        right_len = 1
                                        for j in range(1, len(right)):
                                            if (j % 2 == 1 and right[j] >= right[j - 1]) or (j % 2 == 0 and right[j] <= right[j - 1]):
                                                right_len += 1
                                            else:
                                                right_len = 1
                                        # Check if the left and right can be merged
                                        # Check the left end and right end
                                        if left[-1] <= right[0]:
                                            # Check if the left and right parts can be merged
                                            # Check the left part
                                            left_len = 1
                                            for j in range(1, len(left)):
                                                if (j % 2 == 1 and left[j] >= left[j - 1]) or (j % 2 == 0 and left[j] <= left[j - 1]):
                                                    left_len += 1
                                                else:
                                                    left_len = 1
                                            # Check the right part
                                            right_len = 1
                                            for j in range(1, len(right)):
                                                if (j % 2 == 1 and right[j] >= right[j - 1]) or (j % 2 == 0 and right[j] <= right[j - 1]):
                                                    right_len += 1
                                                else:
                                                    right_len = 1
                                            # Check if the left and right can be merged
                                            # Check the left end and right end