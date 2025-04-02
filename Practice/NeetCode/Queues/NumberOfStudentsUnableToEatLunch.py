from collections import Counter


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        res = len(students)  # Initialize res to the number of students
        # Create a counter to count the preferences of students
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:  # If there are students who prefer the current sandwich
                res -= 1  # Decrement the count of students who need to be served
                # Decrement the count of students who prefer this type of sandwich
                cnt[s] -= 1
            else:
                return res  # If no student prefers the current sandwich, return the number of students left
        # This below line of execution is called only on positive scenarios where all the student are fed
        # Basically it return only 0
        return res  # Return the number of students left after trying to serve all sandwiches


solution = Solution()
print(solution.countStudents([1, 1, 0, 0], [0, 1, 1, 1]))
