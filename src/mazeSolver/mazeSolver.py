import Locater
from collections import deque

x_start = 0
y_start = 0

x_goal = 5
y_goal = 10


def main():
    print("I am solving the maze")

    locator_initial = Locater.Locater(x_start, y_start)
    locator_goal = Locater.Locater(x_goal, y_goal)

    print("The final goal is: ", locator_goal)
    print("The initial state is: ", locator_initial)

    visited = []
    stack = deque()

    curr_state = locator_initial

    while True:
        if curr_state == locator_goal:
            print("Current state is: ", curr_state)
            print("Locater state is: ", locator_goal)

            print("We have reached the goal!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break
        else:
            visited.append(curr_state)
            children = curr_state.children(x_goal, y_goal)
            print("Current state is: ", curr_state)
            print("children are: ", children)

            for child in children:
                if child not in visited:
                    stack.append(child)

            if len(stack) == 0:
                print("No solution")
                break

            curr_state = stack.pop()


if __name__ == "__main__":
    main()
