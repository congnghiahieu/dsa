class BrowserHistory:
    # Using stack

    def __init__(self, homepage: str):
        self.current_url = homepage
        self.backward_stack = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.backward_stack.append(self.current_url)
        self.current_url = url
        self.forward_stack = []

    def back(self, steps: int) -> str:
        while steps > 0 and self.backward_stack:
            self.forward_stack.append(self.current_url)
            self.current_url = self.backward_stack.pop()
            steps -= 1

        return self.current_url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.backward_stack.append(self.current_url)
            self.current_url = self.forward_stack.pop()
            steps -= 1

        return self.current_url
