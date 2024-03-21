
def bowling_point_calculator(bowl_str):
    bowl_list = bowl_str.split()
    # ["1-","2-"...]
    total = 0
    is_prev_spare = False
    is_prev_strike = False

    for i in bowl_list:
        # i is frame
        current_frame_total = 0

        #spare checking
        if is_prev_spare and i[0] not in "-X":
            total += int(i[0])
            is_prev_spare = False
        elif i[0] == "X": # would fail if bad input
            is_prev_strike = True
            total += 10
            continue

        for j in i:
            # j is individual throw
            if j not in "-/": # check
                current_frame_total += int(j)

        if i[1] == "/":
            is_prev_spare = True
            current_frame_total = 10
        
        if is_prev_strike: # account for strike points in current two throws
            total += current_frame_total

        total += current_frame_total
    return total