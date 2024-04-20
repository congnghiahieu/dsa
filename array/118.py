class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal_tri: list[list[int]] = [[1]]
        for i in range(1, numRows):
            prev_lv = pascal_tri[i - 1]
            pascal_tri.append(
                [
                    prev_lv[0],
                    *[prev_lv[j] + prev_lv[j + 1] for j in range(0, len(prev_lv) - 1)],
                    prev_lv[-1],
                ]
            )
        return pascal_tri
