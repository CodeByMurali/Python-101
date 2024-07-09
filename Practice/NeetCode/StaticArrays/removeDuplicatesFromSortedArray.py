class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Left pointer keeps track of the index for the next unique element
        # Right pointer traverses over the array
        l = 1

        # Start from index 1 as the 0th index element is always unique
        for r in range(1, len(nums)):
            # Compare if the current element is equal to the previous element
            if nums[r] != nums[r - 1]:
                # Move the unique element to the left index
                nums[l] = nums[r]
                # Increment the left index to serve as a placeholder for the next unique element
                l += 1

        return l
