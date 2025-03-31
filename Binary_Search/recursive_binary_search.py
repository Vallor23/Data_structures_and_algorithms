def recursive_binary_search(numbers, target):
    if len(numbers) == 0:
        return False
    else:
        midpoint = len(numbers) // 2
        if numbers[midpoint] == target:
            return True
        else:
            if numbers[midpoint] < target:
                return recursive_binary_search(numbers[midpoint + 1:], target)
            else:
                return recursive_binary_search(numbers[:midpoint], target)
            
def verify(index):
    """
    Verify the result of the binary search.
    """
    if index:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list.")
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 5)
verify(result)
result = recursive_binary_search(numbers, 11)
verify(result)
