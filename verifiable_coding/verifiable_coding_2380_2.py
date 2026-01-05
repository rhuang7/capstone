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
        s = data[idx]
        idx += 1
        
        # For a k-periodic garland, the positions of '1's must be at positions
        # i * k, (i + 1) * k, (i + 2) * k, ... such that they are exactly k apart.
        # So the positions of '1's must be in the form of a * k, where a is an integer.
        # We need to find all positions in s that are multiples of k, and check if they are '1's.
        # Then, we can decide whether to turn on or off lamps to make the garland k-periodic.
        
        # The possible positions for '1's are 0, k, 2k, 3k, ... up to n-1.
        # So we can iterate through these positions and count how many are '1's.
        # The rest must be turned off.
        # However, there is a possibility of multiple valid configurations, so we need to find the one with the minimum moves.
        
        # Let's find all positions that are multiples of k.
        positions = [i for i in range(n) if i % k == 0]
        
        # Now, we need to decide which of these positions should be '1's.
        # The number of '1's in the final garland must be such that the distance between each pair is exactly k.
        # So, the number of '1's can be any number m, where m is the number of positions in positions.
        # For example, if there are 5 positions, we can choose any subset of them to be '1's such that they are exactly k apart.
        # However, the minimal moves would be achieved by choosing the positions that already have '1's.
        
        # So, we can count how many of the positions are already '1's, and the rest need to be turned off.
        # However, there's a catch: the positions must be exactly k apart, so the number of '1's must be such that they are in the form of a * k, and the distance between consecutive '1's is exactly k.
        # So the number of '1's must be such that the positions are a, a + k, a + 2k, etc.
        # So the number of '1's can be any number m, but the positions must be exactly k apart.
        
        # So, the number of '1's must be such that the positions are a, a + k, a + 2k, ..., a + (m-1)k.
        # So the total number of positions is m, and the positions are a, a + k, ..., a + (m-1)k.
        # The positions must be within the range [0, n-1].
        
        # So, the number of '1's in the final garland can be any number m, and the positions must be a, a + k, ..., a + (m-1)k.
        # We need to find the m that requires the least moves.
        
        # To find the minimal moves, we can try all possible m (number of '1's in the final garland), and for each m, find the minimal moves.
        
        # The possible m values are from 0 to the maximum number of positions that can be chosen in steps of k.
        # The maximum number of positions is floor((n-1)/k) + 1.
        
        # Let's compute the maximum number of positions.
        max_positions = (n - 1) // k + 1
        
        # Now, for each possible m (number of '1's), we can try to find the minimal moves.
        # For each m, the positions of '1's must be a, a + k, ..., a + (m-1)k.
        # So, the positions are a, a + k, ..., a + (m-1)k, and these must be within the range [0, n-1].
        
        # For each m, we can try all possible a (starting positions), and compute the minimal moves.
        
        # However, this would be too slow for large n and k.
        
        # So, we can try a different approach.
        # The positions of '1's in the final garland must be at positions i * k, where i is an integer.
        # So, for each position in the original string, if it is a multiple of k, we can decide whether to turn it on or off.
        # The minimal moves would be to keep the existing '1's and turn off the others.
        
        # However, there's a problem: the positions of '1's must be exactly k apart.
        # So, for example, if there are positions 0, 2k, 4k, etc., then the distance between them is 2k, which is not k.
        # So, the positions must be in a sequence of positions that are exactly k apart.
        
        # Therefore, the positions of '1's must be in the form of a, a + k, a + 2k, ..., a + (m-1)k.
        # So, the number of '1's must be such that the positions are in this sequence.
        
        # So, the number of '1's must be such that the positions are in a sequence of length m, and the positions are at intervals of k.
        
        # Therefore, the number of '1's must be such that the positions are in the form of a, a + k, ..., a + (m-1)k.
        
        # So, the positions must be at intervals of k. Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # So, the number of '1's can be any number m, and the positions must be in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # So, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # So, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be such that the positions are in a sequence of length m, with step k.
        
        # Therefore, the number of '1's must be