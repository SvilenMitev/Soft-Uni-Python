Initial_array = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        break
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(Initial_array) -1:
            end_index = len(Initial_array) -1
        merged_elements = ''.join(Initial_array[start_index:end_index+1])
        Initial_array[start_index:end_index+1] = [merged_elements]

    elif command[0] == 'divide':
        index = int(command[1])
        partition_index = int(command[2])
        element = Initial_array[index]
        divided_partition = []
        partition_length = len(element) // partition_index
        for current_element in range(partition_index):
            if current_element != partition_index -1:
                divided_partition.append(element[current_element*partition_length:(current_element + 1) * partition_length])
            else:
                divided_partition.append(element[current_element*partition_length:])
        Initial_array[index:index+1] = divided_partition

print(' '.join(Initial_array))