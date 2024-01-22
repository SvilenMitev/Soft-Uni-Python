from collections import deque
# You are learning how to make milkshakes.

chocolete = list(map(int, input().split(', ')))
milk_cups = deque(map(int, input().split(', ')))
count = 0
while chocolete and milk_cups and count != 5:
    if chocolete[-1] == milk_cups[0]:
        current_choko = chocolete.pop()
        current_milk = milk_cups.popleft()
        count += 1

    elif chocolete[-1] <= 0 and milk_cups[0] <= 0:
        current_choko = chocolete.pop()
        current_milk = milk_cups.popleft()
    elif chocolete[-1]  <= 0:
        chocolete.pop()
    elif milk_cups[0] <= 0:
        milk_cups.popleft()
    elif chocolete[-1] != milk_cups[0]:
        chocolete[-1] -= 5
        milk_cups.append(milk_cups.popleft())


if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolete == 0:
    print("Chocolate: empty")
else:
    print(f"Chocolate: {', '.join(str(x) for x in chocolete) or 'empty'}")
if milk_cups == 0:
    print("Milk: empty")
else:
    print(f"Milk: {', '.join(str(x) for x in milk_cups) or 'empty'}")
