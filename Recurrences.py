#Concrete Mathematics
def hanoi(n_disks):
    """Number of moves to move n_disks
    in the tower of Hanoi problem
    """
    if n_disks == 0:
        return 0
    return 2 * hanoi(n_disks - 1) + 1

# print("Hanoi 0 ", hanoi(0))
# print("Hanoi 1 ", hanoi(1))
# print("Hanoi 2 ", hanoi(2))
# print("Hanoi 3 ", hanoi(3))
# print("Hanoi 7 ", hanoi(7))
# print("Hanoi 8 ", hanoi(8))
# print("Hanoi 64", hanoi(64))

