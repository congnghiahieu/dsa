class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            # Assume that positive number go to right, negative number go left
            # Ex: stack = [..., 10] vs n = -5. Imagine that 10 is on the left and go to right, -5 on the right and go to left. So they meet
            # Ex: stack = [..., -10] vs n = 5. Imagine that -10 is on the left and go to left, 5 on the right and go to right. So they never meet
            if (
                not stack
                or (stack[-1] * asteroid > 0)
                or (stack[-1] < 0 and asteroid > 0)
            ):
                stack.append(asteroid)
                continue

            # At here we handle the case stack = [..., 10] vs n = -5.
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroid)

        return stack
