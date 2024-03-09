import os
from PIL import Image

def listFiles(directory):
    files = os.listdir(directory)
    # for file in files:
    #     print(file)
    return files

# def cutArea(boxstart, boxend):
#     startX = boxstart[0]
#     startY = boxstart[1]
#     endX = boxend[0]
#     endY = boxend[1]
#     return startX, startY, endX, endY

def cropImage(directory, crop_box, files):
    for file in files:
        path = os.path.join(directory, file)
        img = Image.open(path)
        cropped_img = img.crop(crop_box)
        print("\nCropping", file)
        file_name, file_extension = os.path.splitext(file)
        new_name = f"{file_name}_{suffix}{file_extension}"
        new_directory = os.path.join(directory, "Cropped_Images")
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        new_path = os.path.join(new_directory, new_name)
        try:
            cropped_img.save(new_path)
            print("Saving", new_name, "in directory:", new_directory)
        except:
            print("Error. File not saved.")

directory = input("Enter directory path: ")
# boxstart = input("Please specify start position as: X Y\n   Start position: ").split()
# boxend = input("Please specify end position as: X Y\n   End position: ").split()

crop_box = input("Please specify start position as: X Y\n   Start position: ")
crop_box += " " + input("Please specify end position as: X Y\n   End position: ")
crop_box = crop_box.split()
print(crop_box)
for x in range(len(crop_box)):
    crop_box[x] = int(crop_box[x])
suffix = "cr"

# input_image_path = ""
# output_image_path = ""


# box = box.split()



# val = 0
# while val < 4:

files = listFiles(directory)
cropImage(directory, crop_box, files)
# crop_box = input

# print(startX, startY, endX, endY)

