number_of_input = int(input())
music_dictonary = {}

for _ in range(number_of_input):
    music_input = input().split("|")
    piece = music_input[0]
    composer = music_input[1]
    key = music_input[2]
    music_dictonary[piece] = [composer, key]

while True:
    command = input().split("|")
    if command == ["Stop"]:
        break
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in music_dictonary:
            print(f"{piece} is already in the collection!")
        else:
            music_dictonary[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in music_dictonary:
            del music_dictonary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in music_dictonary:
            for key, values in music_dictonary.items():
                if key == piece:
                    values.pop()
                    values.append(new_key)
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, values in music_dictonary.items():
    piece = key
    composer = values[0]
    key = values[1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")
