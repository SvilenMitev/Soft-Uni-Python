from collections import deque

people =deque([])
while True:
    current_input = input()
    if current_input == "End":
        break
    elif current_input == "Paid":
        for i in range (len(people)):
            print(people.popleft())
    else:
        people.append(current_input)
print(f"{len(people)} people remaining.")