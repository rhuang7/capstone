def check(candidate):
    assert candidate(5,10,1,5) == (1,10)
    assert candidate(3,5,7,9) == (3,9)
    assert candidate(1,5,2,8) == (1,8)


def select_non_overlapping_points(range1, range2):
    """
    Selects points from two ranges such that no point lies in both ranges.
    """
    # Extract start and end of each range
    start1, end1 = range1
    start2, end2 = range2

    # Check if ranges overlap
    if end1 < start2 or end2 < start1:
        # Ranges do not overlap, return both ranges
        return [range1, range2]
    else:
        # Ranges overlap, return the non-overlapping parts
        # Find the overlapping part
        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)

        # Split into non-overlapping parts
        part1 = (start1, overlap_start - 1) if start1 < overlap_start else None
        part2 = (overlap_end + 1, end1) if end1 > overlap_end else None
        part3 = (start2, overlap_start - 1) if start2 < overlap_start else None
        part4 = (overlap_end + 1, end2) if end2 > overlap_end else None

        # Collect non-overlapping parts
        non_overlapping = []
        if part1:
            non_overlapping.append(part1)
        if part2:
            non_overlapping.append(part2)
        if part3:
            non_overlapping.append(part3)
        if part4:
            non_overlapping.append(part4)

        return non_overlapping

check(select_non_overlapping_points)