team_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
Team_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
games_is_terminated = False
card_received = input()
my_list = card_received.split()
for i in (my_list):
    if i in team_A:
        team_A.remove(i)
    if i in Team_B:
        Team_B.remove(i)
    if len(team_A) < 7 or len(Team_B) < 7:
        games_is_terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(Team_B)}")
if games_is_terminated:
    print("Game was terminated")