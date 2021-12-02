#Concrete Mathematics
import math

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


# print("regions_in_plane: ", regions_in_plane(0))
# print("regions_in_plane: ", regions_in_plane(1))
# print("regions_in_plane: ", regions_in_plane(2))
# print("regions_in_plane: ", regions_in_plane(3))
# print("regions_in_plane: ", regions_in_plane(4))
# print("regions_in_plane: ", regions_in_plane(7))

def josephus(n_people):
    """
    Simply stated how many people are
    left in a circle of n_people
    after the elimination of every kth person
    Closed form: josephus(2^m + L) = 2L + 1
    where L = n_people - 2 ^ m
    where m is the largest power such that 2 ^ m
    is not greater than n_people.

    Example:
    josephus(100) = 2 * 36 + 1 = 73
    100 =  2 * 6 + 36 where m = 6 and L = 100 - 2 ^ 6
    """
    if n_people == 1:
        return 1
    if n_people % 2 == 0:
        return 2 * josephus(n_people//2) - 1
    else:
        return 2 * josephus(n_people//2) + 1


# print("josephus(n_people): ", josephus(1))
# print("josephus(n_people): ", josephus(2))
# print("josephus(n_people): ", josephus(3))
# print("josephus(n_people): ", josephus(4))
# print("josephus(n_people): ", josephus(5))
# print("josephus(n_people): ", josephus(6))
# print("josephus(n_people): ", josephus(7))

def comparisons(n):
    """
    The total number of comparisons
    needed to recursively sort
    n records by halving the input
    and subsequently merging it
    to its final sorted form
    """
    if n == 1:
        return 0
    return comparisons(math.ceil(n/2)) + comparisons(math.floor(n/2)) + n - 1


def distribute(n_things, m_groups,result=[]):
    """
    partition n things into m groups
    as equally as possible
    """
    if m_groups == 1:
        return
    things_group = math.ceil(n_things/m_groups)
    n_next = n_things - things_group 
    result.append((n_next,things_group))
    m_next = m_groups - 1
    distribute(n_next, m_next, result)
    return result

def gcd(m,n):
    if m == 0:
        return n
    return gcd(n % m, m)

def sterling_second(n,k):
    """
    Stirling numbers of the second kind
    The number of ways to partition 
    a set of n things into k nonempty subsets.
    """
    if n == 0 or k == 0:
        if k == 0 and n != 0:
            return 0
        if n == 0 and k != 0:
            return 0
        if n == 0 and k == 0:
            return 1
    return k * sterling_second(n - 1, k) + sterling_second(n - 1, k - 1)


# if __name__ == "__main__":
#     for n in range(10):
#         for k in range(0,n + 1):
#             print(sterling_second(n,k), end=" ")
#         print()

def sterling_first(n,k):
    """
    Stirling numbers of the first kind
    counts the number of ways to arrange n objects into k
    cycles instead of subsets. We verbalize by saying n cycle k."
    """
    if n == 0 or k == 0:
        if k == 0 and n != 0:
            return 0
        if n == 0 and k != 0:
            return 0
        if n == 0 and k == 0:
            return 1
    return (n - 1)* sterling_first(n - 1, k) + sterling_first(n - 1, k - 1)


# if __name__ == "__main__":
#     for n in range(10):
#         for k in range(0,n + 1):
#             print(sterling_first(n,k), end=" ")
#         print()
    





