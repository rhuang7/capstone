import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K, M = map(int, data[idx:idx+3])
        idx += 3
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = list(map(int, data[idx:idx+N]))
        idx += N
        C = list(map(int, data[idx:idx+K]))
        idx += K
        D = list(map(int, data[idx:idx+M]))
        idx += M
        
        # For each day, calculate the potential reduction in uncompleted tasks
        # Uncompleted tasks = A[i] - B[i]
        # We can reduce this by using a white button (if A[i] >= x)
        # Or increase B[i] by using a black button (if B[i] + x <= A[i])
        
        # Sort white buttons in descending order for greedy approach
        C.sort(reverse=True)
        # Sort black buttons in descending order for greedy approach
        D.sort(reverse=True)
        
        # For each day, we can use a white or black button
        # We need to select which buttons to use to minimize the total uncompleted tasks
        
        # We'll use a priority queue to track the potential gains from using a button on a day
        # For each day, we can use a white button (if possible) or a black button (if possible)
        # We'll prioritize using buttons that give the maximum gain
        
        # For each day, compute the current uncompleted tasks
        uncompleted = [A[i] - B[i] for i in range(N)]
        
        # We'll use a max heap to track the potential gains from using a button on a day
        # The heap will store (-gain, day_index)
        # We'll use a set to track which buttons have been used
        white_used = set()
        black_used = set()
        heap = []
        
        # For each day, compute the possible gains from using a white or black button
        for i in range(N):
            # Possible gain from using a white button
            if A[i] >= C[0] and C[0] not in white_used:
                gain = C[0]
                white_used.add(C[0])
                heapq.heappush(heap, (-gain, i))
            # Possible gain from using a black button
            if B[i] + D[0] <= A[i] and D[0] not in black_used:
                gain = D[0]
                black_used.add(D[0])
                heapq.heappush(heap, (-gain, i))
        
        # Now, we'll use the buttons that give the maximum gain
        total_gain = 0
        used_white = set()
        used_black = set()
        
        while heap:
            gain, i = heapq.heappop(heap)
            gain = -gain
            if gain == 0:
                break
            # Check if the button was already used
            if gain in used_white or gain in used_black:
                continue
            # Check if the button is still valid for this day
            if gain in C and C.index(gain) not in used_white:
                used_white.add(gain)
                total_gain += gain
            elif gain in D and D.index(gain) not in used_black:
                used_black.add(gain)
                total_gain += gain
        
        # The minimum possible uncompleted tasks is the sum of uncompleted tasks minus the total gain
        total_uncompleted = sum(uncompleted) - total_gain
        results.append(total_uncompleted)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()