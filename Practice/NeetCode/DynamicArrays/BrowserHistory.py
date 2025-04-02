class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]  # Initialize with the homepage
        self.current_index = 0     # The current page index in the history
        self.forward_stack = []    # Stack to handle forward navigation

    def visit(self, url: str) -> None:
        # Clear forward history because we are visiting a new page
        self.forward_stack = []
        # Move to the new page and update history
        self.current_index += 1
        # Extend history if necessary
        if self.current_index < len(self.history):
            self.history = self.history[:self.current_index + 1]
        self.history.append(url)

    def back(self, steps: int) -> str:
        # Move back in history
        # Cannot move back more than the current index
        steps = min(steps, self.current_index)
        # Add current page to forward stack
        self.forward_stack.append(self.history[self.current_index])
        self.current_index -= steps
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        # Move forward in history
        # Cannot move forward more than the length of the forward stack
        steps = min(steps, len(self.forward_stack))
        self.current_index += steps
        # Ensure not to exceed the history bounds
        if self.current_index >= len(self.history):
            self.current_index = len(self.history) - 1
        # Move pages from forward stack to history
        while steps > 0:
            self.forward_stack.pop()  # Remove from forward stack
            steps -= 1
        return self.history[self.current_index]
