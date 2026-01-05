import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        peaks = []
        for i in range(1, n-1):
            if a[i-1] < a[i] and a[i] > a[i+1]:
                peaks.append(i)
        
        max_peaks = -1
        best_l = 0
        
        for i in range(n - k + 1):
            current_peaks = 0
            for j in range(i + 1, i + k - 1):
                if peaks.count(j) > 0:
                    current_peaks += 1
            if current_peaks > max_peaks or (current_peaks == max_peaks and i < best_l):
                max_peaks = current_peaks
                best_l = i
        
        results.append(f"{max_peaks + 1} {best_l}")
    
    print("\n".join(results))