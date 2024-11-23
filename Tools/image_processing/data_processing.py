import json

with open("defaults.json", "r") as f:
    data = json.load(f)

# # SCREEN SIZES
# screen_sizes = data["screen_sizes"]
# main_screen = data["screen_sizes"]["main_screen"]
# sec_screen_1 = data["screen_sizes"]["secondary_screen_1"]
# sec_screen_2 = data["screen_sizes"]["secondary_screen_2"]


# SCREEN COORDINATES
screen_order_data = dict(left = 0, middle = 0, right = 0)
for screen in data["screen_alignment"].keys():
    if data["screen_alignment"][screen][0] == "left":
        screen_order_data["middle"] += data["screen_sizes"][screen][0]
        screen_order_data["right"] += data["screen_sizes"][screen][0]
    elif data["screen_alignment"][screen][0] == "middle":
        screen_order_data["right"] += data["screen_sizes"][screen][0]
    elif data["screen_alignment"][screen][0] == "right":
        continue

screen_coordinates = dict()
for screen in data["screen_alignment"].keys():
    screen_coordinates[screen] = [screen_order_data[data["screen_alignment"][screen][0]], data["screen_alignment"][screen][1]]
print(screen_coordinates)

# print(x_middle, x_right)

# alignment_data = dict(left = 0, middle = 0, right = 0)
# screen_x = 0
# for screen in alignment.keys():
#     if alignment[screen][0] == "left":
#         screen_x += data["screen_sizes"][screen][0]
#     elif alignment[screen][0] == "middle":
#         alignment_data["middle"] = screen_x - 1
#         screen_x += data["screen_sizes"][screen][0]
#     elif alignment[screen][0] == "right":
#         alignment_data["right"] = screen_x - 1
# print(alignment_data)

# for x in alignment.keys():
#     if alignment[x][0] == "left":
#         alignment_data[x] = 0
#     else: 
#         alignment_data[x] = 1

# main_screen_relative_x = SEC_SCREEN_1_X * alignment_data["secondary_1"] + SEC_SCREEN_2_X * alignment_data["secondary_2"]
# sec_screen_1_relative_x = MAIN_SCREEN_X * alignment_data["main"] + MAIN_SCREEN_2_X * alignment_data["secondary_2"]

# SCREEN COORDINATES
# Left screen

# MAIN_SCREEN_X0 = 
# MAIN_SCREEN_Y0 = 
# MAIN_SCREEN_X1 = 
# MAIN_SCREEN_Y1 = 


# LEFT_Y_TOP = 360
# LEFT_Y_BOTTOM = MAIN_Y - (360 - Y_DIFF_LEFT)

# LEFT_START_X = 0
# LEFT_START_Y = LEFT_Y_BOTTOM
# LEFT_END_X = LEFT_X - 1
# LEFT_END_Y = LEFT_Y_BOTTOM - 1

# # Right screen
# RIGHT_START_X = 0
# LEFT_START_Y = LEFT_Y_BOTTOM
# LEFT_END_X = LEFT_X - 1
# LEFT_END_Y = LEFT_Y_BOTTOM - 1