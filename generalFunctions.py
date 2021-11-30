def stern_brocot(m, n):
    """
    prints the left "L" and right "R"
    branching to take when an element
    in the stern-brocot tree

    eg. stern_brocot(5,7) = LRRL
    for more on stern brocot 
    check out concrete mathematics by knuth, patashnik

    """
    while m != n:
        if m < n:
            print("L")
            n = n - m
        else:
            print("R")
            m = m - n