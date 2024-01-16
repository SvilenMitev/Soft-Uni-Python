from collections import deque

amount_of_food = int(input())


requested_food = deque(int(i) for i in input().split())

print(max(requested_food))

while True:
    if len(requested_food) == 0:
        print("Orders complete")
        break
    if amount_of_food >= requested_food[0]:
        current_order = requested_food.popleft()

        amount_of_food -= current_order
    else:
        print(f"Orders left: {' '.join(map(str,requested_food))}")
        break

        