string_input = input()
deck_of_cards = string_input.split()
count_of_shuffels = int(input())
for shuffle in range(count_of_shuffels):
    half_of_the_deck = len(deck_of_cards) // 2

    left_side = deck_of_cards[0:half_of_the_deck]
    right_side = deck_of_cards[half_of_the_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_side)):
        deck_after_shuffling.append(left_side[card_index])
        deck_after_shuffling.append(right_side[card_index])
        deck_of_cards = deck_after_shuffling
print(deck_after_shuffling)