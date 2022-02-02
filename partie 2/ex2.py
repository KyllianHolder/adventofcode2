with open("input.txt", "r") as f:
    data = f.read()
    formatted_data = str.splitlines(data)
    horinzontal_pos = 0
    vertical_pos = 0
    aim = 0
    for row in formatted_data:
        guiding = row.split()
        if(guiding[0] == "down"):
            aim = aim + int(guiding[1])
        elif(guiding[0]== "up"):
            aim = aim - int(guiding[1])
        elif(guiding[0] == "forward"):
            horinzontal_pos = horinzontal_pos + int(guiding[1])
            vertical_pos = vertical_pos + (int(guiding[1])*aim) 
    final_pos = horinzontal_pos * vertical_pos
    print(final_pos)
