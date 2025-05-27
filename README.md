# Technical Test - R&D Team Solutions

## Overview

Solutions for two algorithmic problems from the Miva Open University R&D Team coding test.

### 1. Plus One

 **Problem** : Increment a large integer represented as an array of digits by one.

 **Algorithm** : Simulate addition with carry propagation from right to left.

 **Time Complexity** : O(n)

 **Space Complexity** : O(1) in-place, O(n) worst case

### 2. Alternate Min-Max Rearrangement

 **Problem** : Rearrange array so elements alternate between smallest and largest remaining values.

 **Algorithm** : Sort array, then use two pointers to alternate between minimum and maximum values.

 **Time Complexity** : O(n log n)

 **Space Complexity** : O(n)

## Usage

```python
# Task 1 - Plus One
from task1 import plus_one
result = plus_one([1, 2, 3])  # Returns [1, 2, 4]

# Task 2 - Alternate Min-Max
from task2 import alternate_min_max
result = alternate_min_max([13, 7, 8, 3, 2, 10, 15, -1])
# Returns [-1, 15, 2, 13, 3, 10, 7, 8]
```

## Testing

Run individual test files to verify solutions:

```python
python task1.py
python task2.py
```


## Files

* `task1.py` - Plus One implementation with test cases
* `task2.py` - Alternate Min-Max implementation with test cases
