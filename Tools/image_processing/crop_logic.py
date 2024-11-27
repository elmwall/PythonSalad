import os
from PIL import Image
from datetime import datetime


# def is_image(format):
#     accepted_formats = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}
#     if not format in accepted_formats:
#         raise ValueError(f"{format} is not recognized as a valid format for processing.")


# Identify images and store information
def target_files(directory):
    accepted_formats = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}

    # Find all files in selected folder and sort by time
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]   
    files.sort(key=lambda f: os.path.getmtime(os.path.join(directory, f)), reverse=True)
 
    # Create a dictionary with only accepted image formats
    file_range = list(range(len(files)))
    file_dict = {str(x + 1): files[x] for x in file_range if os.path.splitext(files[x])[1].lower() in accepted_formats}

    return file_dict


# Selection of file(s) for processing
def select_file(file_dict):
    for x, y in file_dict.items():
        if int(x) == 11: break
        print(f"  {x}:  {y}")
    selection = input("\nPlease enter file number. \nTo show full list, enter 0. \nSelection: ")
    print("Select files by number in correct format: \n  - Individual: single numeral \n  -Interval: separate by dash, first-last \n  - Multiple specific images: separate by comma")
    selection = input("\n  Selection: ")    # TODO: Update selection processing
    if selection == "0":
        for x, y in file_dict.items():
            print(f"  {x}:  {y}")
        selection = input("\nPlease enter file number. \nTo show full list, enter 0. \nSelection: ")

    if selection in file_dict.keys():
        file_path = os.path.join(path, file_dict[selection])
    image = Image.open(file_path)
    image.show()



# format = ".jpg"
# try:
#     is_image(format)
# except ValueError as e:
#     print(e)

path = r"C:\Users\jelmw\Pictures\Screenshots"
batch_path = r"C:\Users\jelmw\Pictures\Screenshots\batch"
output_path = r"C:\Users\jelmw\Documents\Programmering\PythonSalad\Tools\image_processing\output"

# print(path)
file_dict = target_files(path)
select_file(file_dict)

# os.startfile(file_path)
# print(files)
# print(files_with_dates)