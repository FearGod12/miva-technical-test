from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    Increments a large integer represented as an array of digits by one.
    This function takes an array of digits, where each element represents a single digit of a large integer,
    and increments the integer by one. The result is returned as a new array of digits.
    Args:
        digits: List[int] - array representing digits of a large integer

    Returns:
        List[int] - array representing the incremented integer
    Example:
        >>> plus_one([1, 2, 3])
        [1, 2, 4]
        >>> plus_one([9])
        [1, 0]
        >>> plus_one([1, 9, 9])
        [2, 0, 0]
    """
    # Start from the rightmost digit
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry

        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break

    # If we still have a carry, we need to add a new digit at the front
    if carry:
        return [1] + digits

    return digits

# Example usage:
print(plus_one([1, 9, 9, 9, 9]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))
