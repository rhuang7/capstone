def check(candidate):
    assert candidate(23.5,67.5,25.5,69.5)==12179.372041317429
    assert candidate(10.5,20.5,30.5,40.5)==6069.397933300514
    assert candidate(10,20,30,40)==6783.751974994595


def calculate_distance(lat1, lon1, lat2, lon2):
    from math import radians, sin, cos, sqrt, atan2

    # Convert degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6371 * c  # Radius of Earth in kilometers

    return distance

check(calculate_distance)