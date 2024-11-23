# MODULES
import os
import sys
from PIL import Image



# FUNCTIONS
# Standard response to input queries
def queryExit(queryInput):
    if queryInput not in ("1", "2"):
        sys.exit()

# Chech whether target file is an image
def isImage(extension):
    # List of accepted extensions
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    return extension in image_extensions

# Perform crop and save in a subfolder 
def main(directory, files, actions, actionQuery):
    errors = set()  # Create set for storing errors

    # Run class function to obtain required specifications
    spec = actions[actionQuery].spec()

    # Loop through files in folder
    for file in files:
        # Navigate to file and register extension
        path = os.path.join(directory, file)
        file_extension = os.path.splitext(file)[1].lower()  # Extract extension

        if isImage(file_extension): # Only perform action for images
            try:
                # Run class function to obtain info for performing modification
                modified_img, changeFormat = actions[actionQuery].action(path, spec)
                print("\n" + actions[actionQuery].statement, file)   # Print action performed
                
                # Navigate to or create folder
                new_directory = os.path.join(directory, actions[actionQuery].folder)
                if not os.path.exists(new_directory):
                    os.makedirs(new_directory)

                # Save modified image
                if changeFormat:    # Naming for converted image
                    name = os.path.splitext(file)[0]    # Extract name
                    file = f"{name}.{changeFormat.lower()}" # Rename with new proper extension
                    # Set new file path
                    new_path = os.path.join(new_directory, file)
                    modified_img.save(new_path, changeFormat)
                else:   # Naming for cropped image
                    # Set new file path
                    new_path = os.path.join(new_directory, file)
                    modified_img.save(new_path)
                print("Saving", file)
                modified_img.close()
            except Exception as e:
                print("Error occurred:", e)
                errors.add(file)
                print("error with file", file)
                continue
        else:
            continue
    print("\nImages saved in directory:", new_directory)    # Confirmation of new directory
    return errors



# CLASSES
# Base class
class Modification:
    def __init__(self):
        # Specify variable names for new folder and message output
        self.folder = ""
        self.statement = ""

# Cropping class
class Crop(Modification):
    def __init__(self):
        super().__init__()
        self.folder = "Cropped images"
        self.statement = "Cropping"

    def spec(self):
        # Define crop area
        crop_box = input("Please specify start position as: X Y\n   Start position: ")
        crop_box += " " + input("Please specify end position as: X Y\n   End position: ")
        # Convert to list
        crop_box = crop_box.split()
        # print("\nCrop area:", "\n   X:", crop_box[0], "to", crop_box[2], "\n   Y:", crop_box[1], "to", crop_box[3])
        print(f"\nCrop area:\n   X: {crop_box[0]} to {crop_box[2]}\n   Y: {crop_box[1]} to {crop_box[3]}")

        return crop_box

    def action(self, path, crop_box):
        # Convert content to integers
        for x in range(len(crop_box)):
            crop_box[x] = int(crop_box[x])

        # Call for specifik action
        with Image.open(path) as img:
            cropping = img.crop(crop_box)
        return cropping, False


# Conversion class
class Convert(Modification):
    def __init__(self):
        super().__init__()
        self.folder = "Converted images"
        self.statement = "Converting"

    def spec(self):
        convertQuery = input("Which format would you like to convert to?\n   1) .jpeg\n   2) .png\n   Else) Exit\n\n   Selection: ")
        queryExit(convertQuery)
        convertQuery = int(convertQuery) - 1

        return convertQuery

    def action(self, path, convertQuery):
        # Conversion info
        formatList = ["JPEG", "PNG"]
        colorList = ["RGB", "RGBA"]
        
        # Call for specifik action
        with Image.open(path) as img:
            convert = img.convert(colorList[convertQuery])
        format = formatList[convertQuery]
        
        return convert, format
    
    

# INITIAL ENTRIES
# Create class instances and tuple of actions
cropIt = Crop()
modIt = Convert()
actions = (cropIt, modIt)

# Specify action
actionQuery = input("\nWhat modification do you want to perform?\n   1) Crop images\n   2) Convert images\n   Else) Exit\n\n   Selection: ")
queryExit(actionQuery)
actionQuery = int(actionQuery) - 1

# Specify directory and files
directory = input("Enter directory path: ")
files = os.listdir(directory)   # Collect a list of files in stated directory



# PERFORM MAIN FUNCTION
# Perform modification function with established entries
output = main(directory, files, actions, actionQuery)

# End of script, show error reports
if len(output) > 0:
    print("\nErrors encountered with files:")
    for x in output:
        print("  - ", x)
else:
    print(actions[actionQuery].statement, "function performed without issues.")


