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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        # The maximum valid subsegment is the entire array if all K flavors are present
        # Otherwise, it's the maximum length of a subsegment missing at least one flavor
        # We can find the maximum length by checking for each flavor if it's missing in the array
        # If all K flavors are present, the answer is N
        # Otherwise, the answer is N - 1
        # But this is not correct, we need to find the longest subsegment that is missing at least one flavor
        # So we need to find the longest subsegment that does not contain all K flavors
        # This can be done by checking for each flavor if it's missing in the array
        # If any flavor is missing, then the entire array is a valid subsegment
        # So the answer is N if all K flavors are present, else N - 1
        # But this is not correct either, we need to find the longest subsegment that is missing at least one flavor
        # So the correct approach is to find the longest subsegment that does not contain all K flavors
        # This can be done by sliding window approach
        # We can use a sliding window to find the longest subsegment that does not contain all K flavors
        # We can use a frequency dictionary to track the count of each flavor in the window
        # We can also track the number of unique flavors in the window
        # If the number of unique flavors in the window is less than K, then it's a valid subsegment
        # So we can use a sliding window to find the maximum length of such a subsegment
        from collections import defaultdict
        freq = defaultdict(int)
        left = 0
        max_len = 0
        unique = 0
        for right in range(N):
            num = A[right]
            if freq[num] == 0:
                unique += 1
            freq[num] += 1
            while unique >= K:
                left_num = A[left]
                freq[left_num] -= 1
                if freq[left_num] == 0:
                    unique -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        results.append(str(max_len))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()