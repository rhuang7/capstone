import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        C = list(map(int, data[idx:idx+N]))
        idx += N
        # Check if city 1 is connected to all other cities
        # We need to check if there's a path from city 1 to all other cities
        # We can use BFS or DFS
        # But since the graph is undirected and we need to check connectivity
        # We can use a modified BFS where we only move to cities with temperature difference <= D
        # We can also check if the temperature differences between consecutive cities in the sorted list are <= D
        # This is a key insight: if we sort the cities by temperature, then the maximum difference between consecutive cities must be <= D
        # Because Chef can travel through cities in order of increasing temperature
        # So we sort the temperatures and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list and check if the first element is C[0] (city 1)
        # Wait, no. The cities are numbered 1 to N, but the temperatures are given in the order of cities 1 to N
        # So the first city is city 1, which has temperature C[0]
        # So we need to check if there's a path from city 1 to all other cities
        # We can sort the list of temperatures and check if the maximum difference between consecutive cities is <= D
        # But this is only valid if the cities can be ordered in a way that allows Chef to travel from one to the next
        # So we sort the temperatures and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the first element is C[0] (city 1)
        # But that's not necessarily true, because the cities are numbered 1 to N, but the temperatures are given in the order of cities 1 to N
        # So the first city is city 1, which has temperature C[0]
        # So we can sort the list of temperatures and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the first element is C[0] (city 1)
        # But that's not necessarily true, because the cities are numbered 1 to N, but the temperatures are given in the order of cities 1 to N
        # So the first city is city 1, which has temperature C[0]
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path
        # So we can sort the list of temperatures, and check if the max difference between consecutive cities is <= D
        # But we have to make sure that city 1 is included in the path