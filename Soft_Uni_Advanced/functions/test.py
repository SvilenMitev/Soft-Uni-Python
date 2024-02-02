a = 5
b = 6
my_list = [a, b]
my_dict = {}
variable_names = [name for name, value in locals().items() if isinstance(value, int)]
for i in variable_names:
    print(i)
    
print(my_list)

# def get_variable_names():
#     """Return a list of variable names in the local scope that are integers."""
#     variable_names = [a, b]
#     for name, value in locals().items():
#         if isinstance(value, int):
#             variable_names.append(name)
#     return variable_names

# # Example usage:
# a = 5
# b = 6

# # Call the function to get the variable names
# variable_names = get_variable_names()

# # Print the list of variable names
# print(variable_names)