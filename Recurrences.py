#Concrete Mathematics
def hanoi(n_disks):
    """Number of moves to move n_disks
    in the tower of Hanoi problem
    Closed Form: hanoi(n_disks) = 2^n_disks - 1
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


def regions_in_plane(n_lines):
    """
    Maximum number of regions
    defined by n_lines in a plane
    Closed Form: regions_in_planes = (n_lines(n_lines + 1) + 1)/2
    """
    if n_lines == 0:
        return 1
    return regions_in_plane(n_lines - 1) + n_lines

if __name__ == "__main__":
  print("regions_in_plane: ", regions_in_plane(0))
  print("regions_in_plane: ", regions_in_plane(1))
  print("regions_in_plane: ", regions_in_plane(2))
  print("regions_in_plane: ", regions_in_plane(3))
  print("regions_in_plane: ", regions_in_plane(4))
  print("regions_in_plane: ", regions_in_plane(7))

