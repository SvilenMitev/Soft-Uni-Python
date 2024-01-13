from collections import deque
kis_names = deque(input().split())
number_of_toss = int(input()) -1 

while len(kis_names) > 1:
    kis_names.rotate(-number_of_toss)
    removed_kid = kis_names.popleft()
    print(f"Remove {removed_kid}")

print(f"Last is {kis_names.popleft()}")