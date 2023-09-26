number_of_snow_balls = int(input())
highest_number: int = 0
weight = 0
time = 0
quality = 0
for n in range(number_of_snow_balls):
    weight_of_snow_balls = int(input())
    time_to_create_snow_balls = int(input())
    quality_of_snow_balls = int(input())

    calc_snowball = (weight_of_snow_balls/time_to_create_snow_balls) ** quality_of_snow_balls
    if calc_snowball > highest_number:
        highest_number = calc_snowball
        weight = weight_of_snow_balls
        time = time_to_create_snow_balls
        quality = quality_of_snow_balls

print(f"{weight} : {time} = {int(highest_number)} ({quality})")
