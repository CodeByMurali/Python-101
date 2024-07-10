class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # This pointer tracks the position of elements that is not val
        # We can move the non val elements to this position
        k = 0

        # i traverses over the elemnets in num
        for i in range(len(nums)):
            # Perform sorting only when the current element is not equal to val
            # if its val we will just ignore it
            if nums[i] != val:
                # Shift the non val number to the position where k is
                nums[k] = nums[i]
                # increment k only when the number is non val
                k += 1
        return k
