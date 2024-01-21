#     1. Numbers
# First, you will be given two sequences of integer values on different lines. The values of the sequences are separated by a single space between them.
# Keep in mind that each sequence should contain only unique values.
# Next, you will receive a number - N. On the following N lines, you will receive one of the following commands:
#     • "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
#     • "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
#     • "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
#     • "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
#     • "Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise, print "False".
# In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be sorted in ascending order.
# Examples

# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset

first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())
number_of_input = int(input())




for i in range(number_of_input):
    command = input().split()
    if command[0] == "Add" and command[1] == "First":
        for y in command:
            if y.isnumeric():
                first_sequence.add(int(y))
    elif command[0] == "Add" and command[1] == "Second":
        for o in command:
            if o.isnumeric():
                second_sequence.add(int(o))
    elif command[0] == "Remove" and command[1] == "first":
        for _ in command:
            if _.isnumeric():
                if int(_) in first_sequence:
                    first_sequence.remove(int(_))
    elif command[0] == "Remove" and command[1] == "Second":
        for u in command:
            if u.isnumeric():
                if int(u) in second_sequence:
                    second_sequence.remove(int(u))
    elif command[0] == "Check":
        if second_sequence.issubset(first_sequence) or first_sequence.issubset(second_sequence):
            print(True)
        else:
            print(False)
first_sequence = sorted(first_sequence)
second_sequence = sorted(second_sequence)

print(", ".join(map(str, first_sequence)))
print(", ".join(map(str, second_sequence)))