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
        is_rainbow = True
        # Check if the array starts with 1s and ends with 1s
        if A[0] != 1 or A[-1] != 1:
            is_rainbow = False
        else:
            # Count the number of 1s at the beginning
            count1 = 0
            while count1 < N and A[count1] == 1:
                count1 += 1
            # Count the number of 1s at the end
            count1_end = 0
            while count1_end < N and A[N - 1 - count1_end] == 1:
                count1_end += 1
            if count1 != count1_end:
                is_rainbow = False
            else:
                # Check the middle part
                if count1 == 0:
                    is_rainbow = False
                else:
                    # Remove the 1s from the start and end
                    A = A[count1:-count1_end]
                    # Check if the middle part is symmetric and follows the rainbow pattern
                    if len(A) % 2 != 0:
                        is_rainbow = False
                    else:
                        mid = len(A) // 2
                        # Check the first half
                        for i in range(mid):
                            if A[i] != i + 2:
                                is_rainbow = False
                                break
                        if is_rainbow:
                            # Check the second half
                            for i in range(mid):
                                if A[mid + i] != 8 - i:
                                    is_rainbow = False
                                    break
        results.append("yes" if is_rainbow else "no")
    print("\n".join(results))

if __name__ == '__main__':
    solve()