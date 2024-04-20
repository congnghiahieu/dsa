class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        # m is number of row ~ y , n is number of column ~ x
        m, n = len(board), len(board[0])
        already_passed: list[list[bool]] = [[False for _ in range(n)] for _ in range(m)]
        already_passed[0][0] = True

        return self.solve(board, m, n, 0, 0, board[0][0], word, already_passed)

    def solve(
        self,
        board: list[list[str]],
        m: int,
        n: int,
        current_y: int,
        current_x: int,
        current_word: str,
        target_word: str,
        already_passed: list[list[bool]],
    ) -> bool:
        if current_word == target_word:
            return True

        if current_word and current_word[0] != target_word[0]:
            already_passed[current_y][current_x] = True
            current_word = ""

        current_word_last_idx = len(current_word) - 1
        if (
            current_word
            and current_word[current_word_last_idx]
            != target_word[current_word_last_idx]
        ):
            return False

        for choice_y in [-1, 0, 1]:
            for choice_x in [-1, 0, 1]:
                next_y, next_x = current_y + choice_y, current_x + choice_x
                if (
                    self.is_valid_move(m, n, next_y, next_x)
                    and not already_passed[next_y][next_x]
                ):
                    current_word += board[next_y][next_x]
                    already_passed[next_y][next_x] = True

                    if self.solve(
                        board,
                        m,
                        n,
                        next_y,
                        next_x,
                        current_word,
                        target_word,
                        already_passed,
                    ):
                        return True

                    current_word = current_word[0 : len(current_word) - 1]
                    already_passed[next_y][next_x] = False

        return False

    def is_valid_move(self, m: int, n: int, y: int, x: int):
        # m is row ~ y, n is col ~ x
        return 0 <= y <= m - 1 and 0 <= x <= n - 1


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(Solution().exist(board, word))
