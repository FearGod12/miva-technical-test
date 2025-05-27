from typing import List

def alternate_min_max(arr: List[int]) -> List[int]:
    """
    Rearrange array so that first element is smallest, second is largest,
    third is second-smallest, fourth is second-largest, and so on.

    Args:
        arr: List[int] - input array of integers

    Returns:
        List[int] - rearranged array following the min-max pattern

    Example:
        >>> alternate_min_max([13, 7, 8, 3, 2, 10, 15, -1])
        [-1, 15, 2, 13, 3, 10, 7, 8]
    """
    if not arr:
        return []

    # Sort the array to get elements in order
    sorted_arr = sorted(arr)
    result: List[int] = []

    left = 0  # Points to smallest remaining element
    right = len(sorted_arr) - 1  # Points to largest remaining element

    # Alternate between taking from left (min) and right (max)
    for i in range(len(sorted_arr)):
        if i % 2 == 0:  # Even index: take minimum
            result.append(sorted_arr[left])
            left += 1
        else:  # Odd index: take maximum
            result.append(sorted_arr[right])
            right -= 1

    return result

# Example usage:
print(alternate_min_max([13, 7, 8, 3, 2, 10, 15, -1]))
print(alternate_min_max([-5, -12, -1, 7, 14, -7, 3, 6]))
print(alternate_min_max([3, 6, 9, -10, -5, -2, 0, 8]))
print(alternate_min_max([]))
print(alternate_min_max([0,0,0,0,0,0,0]))
