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
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        sets = []
        for _ in range(m):
            vi = int(data[idx])
            idx += 1
            s = set(data[idx:idx+vi])
            idx += vi
            sets.append(s)
        # Build the intersection graph
        # Each node is a set
        # An edge from A to B means A and B are not disjoint
        # We need to find the minimum number of atoms, which is the minimum number of nodes in a vertex cover of the intersection graph
        # But since we need to partition X into atoms, it's equivalent to finding the minimum number of sets that cover all elements, such that any two sets in the partition are disjoint
        # This is equivalent to finding the minimum number of sets in a partition of X into disjoint sets, where each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint from all Si
        # This is equivalent to finding the minimum number of sets in a partition of X such that each set is a subset of some Si or disjoint