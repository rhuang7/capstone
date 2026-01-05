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
            start = i
            end = i + k - 1
            count = 0
            for j in range(start + 1, end):
                if a[j-1] < a[j] and a[j] > a[j+1]:
                    count += 1
            if count > max_peaks or (count == max_peaks and i < best_l):
                max_peaks = count
                best_l = i
        
        results.append(f"{max_peaks + 1} {best_l}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()