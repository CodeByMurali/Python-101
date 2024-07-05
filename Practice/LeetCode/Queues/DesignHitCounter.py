from collections import deque


class DesignHitCounter:

    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.hit_que = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hit_que.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        """
        self.hit_que[0] <= timestamp - 300:
        If the first element in the queue is older than 5 minutes
        This can be identified by finding the difference between the current timestamp passed and 300 seconds
        """
        while self.hit_que and self.hit_que[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)


# Example usage:
hitCounter = DesignHitCounter()
hitCounter.hit(1)
hitCounter.hit(2)
hitCounter.hit(3)
print(hitCounter.getHits(4))  # Output: 3
hitCounter.hit(300)
print(hitCounter.getHits(300))  # Output: 4
print(hitCounter.getHits(301))  # Output: 3
