from collections import defaultdict


class FindTheTownJudge:
    #     def findJudge(self, n: int, trust: list[list[int]]) -> int:
    #         # Edge case: If there are no people, return -1 as there's no judge
    #         if n == 0:
    #             return -1

    #         # Edge case: If there's only one person, they are the judge by default
    #         if n == 1:
    #             return 1

    #         # Initialize trust_count and trusted_by arrays with zeros
    #         # trust_count[i] will count how many people trust person i
    #         # trusted_by[i] will count how many people person i trusts
    #         trust_count = [0] * (n + 1)
    #         trusted_by = [0] * (n + 1)

    #         # Iterate through the trust relationships
    #         for a, b in trust:
    #             # Increment the trust count for person b (trusted by person a)
    #             trust_count[b] += 1
    #             # Increment the trusted by count for person a (trusts person b)
    #             trusted_by[a] += 1

    #         # Iterate through all people from 1 to n
    #         for i in range(1, n + 1):
    #             # Check if person i is trusted by n-1 people and trusts nobody
    #             if trust_count[i] == n - 1 and trusted_by[i] == 0:
    #                 return i  # Person i is the judge

    #         # If no judge is found, return -1
    #         return -1

    # # Create an object of the class
    # judge_finder = FindTheTownJudge()

    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 0:
            return -1

        if n == 1:
            return 1

        incoming = defaultdict(int)
        outcoming = defaultdict(int)

        for src, dst in trust:
            # dst represents the person truseted
            # Here we are counting number of times a person is trusted
            # incoming[dst] represents the number of people who trust person dst.
            incoming[dst] = incoming[dst] + 1

            # outgoing[src] represents the number of people that person src trusts.
            outcoming[src] = outcoming[src] + 1

        for node in trust[1: n-1]:
            # if the node is trusted n-1 times (excludes the town judge) and the node is not trusing any other nodes
            if incoming[node] == n-1 and outcoming[node] == 0:
                return node
        return -1


findTheTownJudge = FindTheTownJudge()

print(findTheTownJudge.findJudge(3, [[1, 3], [2, 3]]))
