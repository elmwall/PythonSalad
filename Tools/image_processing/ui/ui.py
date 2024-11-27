import tkinter
from tkinter import ttk

# WINDOW
# Provide ui window and basic geometry and appearance settings
window = tkinter.Tk()   
window.title("Image Processor")     
window.geometry("800x600")
# window.configure(bg="#102520")

# WIDGETS
# Title
title_label = tkinter.Label(window, text="Image Processor")
# Settings widgets
settings_label = tkinter.Label(window, text="Settings")
settings_action_label = tkinter.Label(window, text="Select action")
# Input widgets
input_files_label = tkinter.Label(window, text="Select files")
input_files_entry = tkinter.Entry(window)
input_files_browse = tkinter.Button(window, text="Browse")
# Crop widgets
crop_label = tkinter.Label(window, text="Crop")
crop_screen_label = tkinter.Label(window, text="Select screen")
crop_area_label = tkinter.Label(window, text="Select area")
# Convert widgets
convert_label = tkinter.Label(window, text="Convert")
# Output widgets
output_destination_label = tkinter.Label(window, text="Destination")
output_destination_entry = tkinter.Entry(window)
output_destination_browse = tkinter.Button(window, text="Browse")
output_format_label = tkinter.Label(window, text="Select format")
# Confirm action widget
run_processing_label = tkinter.Button(window, text="Run")

# label = tkinter.Label(window, text="Select files")


# WIDGET PLACEMENT
# Select geometry manager, options are: pack, place, grid
title_label.grid(row=0, column=0, columnspan=3)
settings_label.grid(row=1, column=0)

input_files_label.grid(row=2, column=0)
input_files_entry.grid(row=2, column=1)
input_files_browse.grid(row=2, column=2)

output_destination_label.grid(row=3, column=0)
output_destination_entry.grid(row=3, column=1)
output_destination_browse.grid(row=3, column=2)

crop_label.grid(row=4, column=0)

convert_label.grid(row=5, column=0)

output_format_label.grid(row=6, column=0)

run_processing_label.grid(row=7, column=2)

# Continuous loop running your ui program
window.mainloop()






# import kivy
# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.label import Label


# class AppLayout(GridLayout):
#     # Initialize infinite keywords
#     def __init__(self, **kwargs):
#         # Call grid layout constructor
#         super(AppLayout).__init__(**kwargs)

#         # Set columns
#         self.cols = 2

#         # Add widgets
#         self.add_widget(Label(text="Name: "))
#         # Add Input box
#         self.name = TextInput(multiline=False)
#         self.add_widget(self.name)

#         # Add widgets
#         self.add_widget(Label(text="Pizza: "))
#         # Add Input box
#         self.name = TextInput(multiline=False)
#         self.add_widget(self.name)


# class MainApp(App):
#     def build(self):
#         return super().build()


# class MainApp(App):
#     def build(self):
#         self.icon = "logo.png"  # TODO: USE OTHER IMAGE

#         main_layout = GridLayout(cols=4, row_force_default=True, row_default_height=40)

        
#         # buttons = [
#         #     ["Settings","Select files","Destination",""],
#         #     ["Crop","Screen","Area",""],
#         #     ["Convert","Format","",""],
#         #     ["Run","","",""],
#         # ]
#         buttons = [
#             ["Settings","Crop","Convert",""],
#             ["Select files","Screen","Format",""],
#             ["Destination","Area","",""],
#             ["Run","","",""],
#         ]
#         field = [""]

#         for row in buttons:
#             h_layout = BoxLayout()
#             for label in row:
#                 button = Button(
#                     text = label, font_size = 25, background_color = "green", pos_hint = {"center_x": 0.5, "center_y": 0.5}
#                 )
#                 button.bind(on_press = self.on_button_press)
#                 h_layout.add_widget(button)
#             main_layout.add_widget(h_layout)


#         self.active = TextInput(background_color = "black", foreground_color = "green")
#         main_layout.add_widget(self.active)

#         # run_function.bind(on_press = self.process_image)  # TODO: define function

#         return main_layout
    
#     def on_button_press(self, instance):
#         current = self.output.text    # TODO: define
#         button_output = instance.text

#         # self.functions = ["Crop", "Convert"]
#         # self.options_crop = ["Select files", "Area", "Destination"]
#         # self.options_crop_areas = ["Main screen", "Secondary screen 1", "Secondary screen 2"]
#         # self.options_convert = ["Format", "Destination"]
#         # self.settings = ["Name screens", "Crop pre-sets", "Default options"]





if __name__ == "__main__":
    MainApp().run()