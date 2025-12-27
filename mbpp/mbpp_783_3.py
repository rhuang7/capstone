def check(candidate):
    assert candidate(255, 255, 255)==(0, 0.0, 100.0)
    assert candidate(0, 215, 0)==(120.0, 100.0, 84.31372549019608)
    assert candidate(10, 215, 110)==(149.26829268292684, 95.34883720930233, 84.31372549019608)


def rgb_to_hsv(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0

    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val

    if max_val == 0:
        h = 0
        s = 0
        v = max_val
    else:
        s = diff / max_val
        if diff == 0:
            h = 0
        else:
            if max_val == r:
                h = (g - b) / diff
            elif max_val == g:
                h = (b - r) / diff + 2
            else:
                h = (r - g) / diff + 4
            h = h % 6

    v = max_val
    return h, s, v

check(rgb_to_hsv)