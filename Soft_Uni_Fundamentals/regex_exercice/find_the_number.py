import re
import time


duration_seconds = 5
start_time = time.time()
end_time = start_time + duration_seconds

match = []
while True:
    current_input = input()
    regex = r'\d+'



    for i in current_input:
        match += re.findall(regex, i)
    if time.time() < end_time:
        break
print("".join(match))


import re


pattern = re.compile(r"\d+")
while True:
    data = input()
    if data:
        matches = pattern.finditer(data)

        for match in matches:
            print(match[0], end=" ")
    else:
        break