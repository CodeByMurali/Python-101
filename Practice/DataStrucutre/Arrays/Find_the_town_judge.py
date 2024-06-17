class FindTheTownJudge:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # Edge case: If there are no people, return -1 as there's no judge
        if n == 0:
            return -1

        # Edge case: If there's only one person, they are the judge by default
        if n == 1:
            return 1

        # Initialize trust_count and trusted_by arrays with zeros
        # trust_count[i] will count how many people trust person i
        # trusted_by[i] will count how many people person i trusts
        trust_count = [0] * (n + 1)
        trusted_by = [0] * (n + 1)

        # Iterate through the trust relationships
        for a, b in trust:
            # Increment the trust count for person b (trusted by person a)
            trust_count[b] += 1
            # Increment the trusted by count for person a (trusts person b)
            trusted_by[a] += 1

        # Iterate through all people from 1 to n
        for i in range(1, n + 1):
            # Check if person i is trusted by n-1 people and trusts nobody
            if trust_count[i] == n - 1 and trusted_by[i] == 0:
                return i  # Person i is the judge

        # If no judge is found, return -1
        return -1


# Create an object of the class
judge_finder = FindTheTownJudge()

# Test case
result = judge_finder.findJudge(3, [[1, 3], [2, 3], [3, 1]])
print(f"Town judge: {result}")  # Output: -1


overflow = start + (end - start) / 2 -> Overflows
In Java, Integer.MAX_VALUE represents the maximum value that an int type can hold, which is
2
31
−
1
2
31
 −1 or 2, 147, 483, 647.

When you add 1 to Integer.MAX_VALUE, it results in integer overflow because the value exceeds the maximum value an int can represent. In Java, integer overflow wraps around using two's complement arithmetic, causing the value to wrap around to the minimum value an int can represent, which is 
−
2
31
−2 
31
  or -2,147,483,648.

So, Integer.MAX_VALUE + 1 is 
−
2
,
147
,
483
,
648
−2,147,483,648.

integer overflow attack
Saga patterns
sidtributed data patterns
Design is important