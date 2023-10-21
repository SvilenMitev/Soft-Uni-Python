days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0
for i in range(1, days_of_plunder+1):
    total_plunder += daily_plunder
    if i % 3 == 0:
        total_plunder += daily_plunder*0.5
    if i % 5 == 0:
        total_plunder *= 0.7
less_plunder = (total_plunder / expected_plunder)*100
if expected_plunder <= total_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {less_plunder:.2f}% of the plunder.")