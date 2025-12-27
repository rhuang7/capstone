def check(candidate):
    assert candidate([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000],6)==3
    assert candidate([100,200,300,400],[700,800,900,1000],4)==4
    assert candidate([5,6,7,8],[4,3,2,1],4)==1


def min_platforms(arrival, departure):
    arrival.sort()
    departure.sort()
    
    platforms = 1
    max_platforms = 1
    i = 0
    j = 0
    
    while i < len(arrival) and j < len(departure):
        if arrival[i] < departure[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        max_platforms = max(max_platforms, platforms)
    
    return max_platforms

check(min_platforms)