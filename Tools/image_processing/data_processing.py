import json


# FUNCTIONS
def load_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Check all data is included, return error message and faulty screen entry.
def validate_data(data, file_path):
    required_keys = {"name", "size_xy", "order_x", "offset_y", "active"}
    for screen in data["screens"]:
        if not required_keys.issubset(screen.keys()):
            raise ValueError(f"Required data for screen '{screen["name"]}' is missing in file: {file_path}")

# Process screen data into coordinate information
def screen_data(data):
    horizontal_data = dict(left = 0, middle = 0, right = 0)
    screen_coordinates = dict()

    # Generate horizontal coordinates, depending on order and sizes of screens
    for screen in data["screens"]:
        order_x = screen["order_x"]
        size_x = screen["size_xy"][0]

        # Identify screen position and gather cumulative x distance
        if order_x == "left":
            horizontal_data["middle"] += size_x
            horizontal_data["right"] += size_x
        elif order_x == "middle":
            horizontal_data["right"] += size_x

    # Use pre-defined and calculated data for final output
    for screen in data["screens"]:
        order_x = screen["order_x"]
        offset_x = horizontal_data[order_x]
        offset_y = screen["offset_y"]
        size = screen["size_xy"]
        is_active = screen.get("active")

        # Create dictionary with lists for start and end coordinates. Subract 1 to account for starting position as 0, 0 (not 1, 1).
        if is_active:
            screen_coordinates[screen["name"]] = [[offset_x, offset_y],[offset_x + size[0] - 1, offset_y + size[1] - 1]]
        else: 
            screen_coordinates[screen["name"]] = None

    return screen_coordinates


# MAIN OPERATION STEPS
file_path = "defaults.json"
data = load_data(file_path)
try:
    validate_data(data, file_path)
except ValueError as e:
    print(e)
    exit(1)

# Final output
screen_coordinates = screen_data(data)
