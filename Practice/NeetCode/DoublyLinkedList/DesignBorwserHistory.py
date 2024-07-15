class LinkedListNode:

    def __init__(self, val, prev=None, nxt=None) -> None:
        self.val = val
        self.prev = prev
        self.nxt = nxt


class BrowserHistory:

    def __init__(self, homepage: str) -> None:
        # Create a new node which is the home page
        # The previous and the next is set to None as the default param of LinkedListNode init is None
        # It will be the current node
        self.cur = LinkedListNode(homepage)

    def visit(self, url: str) -> None:
        # We create a new node, we override the default for the previous pointer to the current node
        # The next pointer is null as there are no nodes after
        self.cur.nxt = LinkedListNode(url, self.cur)
        self.cur = self.cur.nxt

    def back(self, steps: int) -> str:
        # We keep going back until there is no previous node or until steps are exhausted
        # We want to return the home page when the number of steps exceed the actual history
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        # We keep going forward until there is no next node or until steps are exhausted
        # We want to return the last node url when the number of steps exceed the actual history
        while self.cur.nxt and steps > 0:
            self.cur = self.cur.nxt
            steps -= 1
        return self.cur.val


# Dummy invocation for all methods
browser_history = BrowserHistory("homepage.com")
browser_history.visit("page1.com")
browser_history.visit("page2.com")
print(browser_history.back(1))  # Should print "page1.com"
print(browser_history.back(1))  # Should print "homepage.com"
print(browser_history.forward(1))  # Should print "page1.com"
browser_history.visit("page3.com")
print(browser_history.forward(1))  # Should print "page3.com"
print(browser_history.back(2))  # Should print "homepage.com"
