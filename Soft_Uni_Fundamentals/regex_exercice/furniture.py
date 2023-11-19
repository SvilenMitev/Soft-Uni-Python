import re


list_of_items = []
money_spend = 0

regex = r'>>([A-Za-z]+)<<(\d+\.?\d*)!([\d]+)'
while True:
    current_input = input()
    if current_input == 'Purchase':
        break
    matches = re.search(regex, current_input)
    if matches:
        items, price, count = matches.groups()
        list_of_items.append(items)
        money_spend += float(price) * int(count)

print("Bought furniture:")      
for i in list_of_items:
    print(i)
print(f"Total money spend: {money_spend:.2f}")