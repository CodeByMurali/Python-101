def search_rotated_array(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid

        # Check if the left portion is sorted
        if arr[mid] >= arr[l]:
            # If target is within the range of the left sorted portion
            if arr[l] <= target <= arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # Otherwise, the right portion must be sorted
        else:
            # If target is within the range of the right sorted portion
            if arr[mid] <= target <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1  # Target not found


# Example usage
arr = [5, 6, 7, 1, 2, 3, 4]
target = 3
index = search_rotated_array(arr, target)
print(index)  # Output: 5
