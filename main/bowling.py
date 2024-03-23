def frame_score_no_bonus(frame):
    # for use in spares, strikes, and tenth frame scores
    score = 0
    for roll in frame:
        if roll == "X":
            return 10
        if roll == "/":
            return 10
        else:
            score += int(roll)
    return score


def bowling_point_calculator(bowl_str):
    bowl_str = bowl_str.replace("-", "0")
    bowl_list = bowl_str.split()
    # ["1-","2-"...]
    total = 0

    # calculate score for first 9 frames
    for i in range(0, 9):
        frame = bowl_list[i]
        current_frame_total = 0
        # strike handling
        if frame[0] == "X":
            # add next two rolls
            if bowl_list[i + 1] == "X":
                total += 20 + frame_score_no_bonus(bowl_list[i + 2][0])
            else:
                total += 10 + frame_score_no_bonus(bowl_list[i + 1])
            continue  # no second roll this frame
        # spare handling
        if frame[1] == "/":
            total += 10 + frame_score_no_bonus(bowl_list[i + 1][0])
            continue  # no need to look at first roll of frame
        # non spare or strike
        for roll in frame:
            current_frame_total += int(roll)
        total += current_frame_total

    # final frame handling
    for frame in bowl_list[9:]:
        if len(frame) > 2:  # spare
            total += 10 + frame_score_no_bonus(frame[2:])
        else:
            total += frame_score_no_bonus(frame)
    return total
