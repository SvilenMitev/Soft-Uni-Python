# def sorting_cheeses(**kwargs):
#     sorted_dict = sorted(kwargs.items(), key=lambda x: sum(x[1]), x[0])
#     for key, value in kwargs.items():
#         print(key)
#         sorted_values = sorted(value, reverse=True)
#         for i in sorted_values:
#             print(i)


def sorting_cheeses(**kwargs):
    result = ""
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, value in sorted_dict:
        result += key + "\n"
        sorted_values = sorted(value, reverse=True)
        for i in sorted_values:
            result += f"{i}\n"
    return result
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
