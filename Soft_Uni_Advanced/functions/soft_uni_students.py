def softuni_students (*args, **kwargs):
    invalid_list = []
    result = ''
    course_dict = {}
    for i in args:
        if i[0] in kwargs:
            course_dict[i[1]] = kwargs[i[0]]
        else:
            course_dict[i[1]] = "invalid"
    sorted_course_dict = dict(sorted(course_dict.items(), key=lambda x: x[0]))
    for keys , value in sorted_course_dict.items():
        if value == "invalid":
            invalid_list.append(keys)
            continue
    
        result += f"*** A student with the username {keys} has successfully finished the course {value}!" "\n"
    if len(invalid_list) > 0:
        result += f"!!! Invalid course students: {', '.join(invalid_list)}"
    
    return result

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
