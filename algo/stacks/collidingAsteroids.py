def collidingAsteroids(asteroids):
    stack = []
    for asteroid in asteroids:
        # if the asteroid is positive, it will always be added to the stack
        if asteroid > 0:
            stack.append(asteroid)
            continue

        # If the top of the stack is positive and the current asteroid is greater than the top of the stack
        # Means the current asteroid will destroy the top of the stack, so we pop the top of the stack(destroy it)
        while stack and stack[-1] > 0 and abs(asteroid) > abs(stack[-1]):
            stack.pop()

        # If the stack is empty or the top of the stack is negative, we can add the current asteroid to the stack
        # Means the current asteroid will not be destroyed, Because there is no positive asteroid to destroy it
        if not stack or stack[-1] < 0:
            stack.append(asteroid)
        # If the size of the current asteroid is equal to the top of the stack, we pop the top of the stack(destroy it)
        elif abs(asteroid) == abs(stack[-1]):
            stack.pop()

    return stack


asteroids = [5]
print(collidingAsteroids(asteroids))
