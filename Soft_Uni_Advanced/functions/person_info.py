# def get_info(**kwargs):
#   print(kwargs)(kwargs)nt((f"This is {kwargs[name]} from {kwargs} and he is {kwargs} years old" ))
#     # return(f"This is {kwargs[name][0]} from {kwargs[town][0]} and he is {kwargs[age][0]} years old" )

# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


def get_info(**kwargs):
    return(f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old")

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))