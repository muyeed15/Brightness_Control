# modules
import customtkinter as ctk
import screen_brightness_control as sbc
from PIL import Image

# current information
data = {
    "display": 0,
    "theme": "light"
}

# theme
ctk.set_appearance_mode(data["theme"])
ctk.set_default_color_theme("blue")

# app
app = ctk.CTk()

# title
app.title("Brightness Control")

# app resolution
app_width = 410
app_height = 140

# get the screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# calculate the x and y coordinates to center the window
x = (screen_width // 2) - (app_width // 2)
y = (screen_height // 2) - (app_height // 2)

# Set the window's geometry
app.geometry(f"{app_width}x{app_height}+{x}+{y}")

# frame
main_frame = ctk.CTkFrame(app, fg_color="transparent")
main_frame.grid(row=0, column=0)

frame_top = ctk.CTkFrame(main_frame, fg_color="transparent")
frame_top.pack(pady=10)

frame_bottom = ctk.CTkFrame(main_frame, fg_color="transparent")
frame_bottom.pack(pady=10)

settings_frame = ctk.CTkFrame(app, fg_color="transparent")

# # get display resolution
# screen_width = main_frame.winfo_screenwidth()
# screen_height = main_frame.winfo_screenheight()

# top image
top_image = ctk.CTkImage(light_image=Image.open("resources/sun.png"),
                        dark_image=Image.open("resources/moon.png"),
                        size=(56, 56))

top_image_label = ctk.CTkLabel(frame_top, image=top_image, text="")
top_image_label.grid(row=0, column=0, padx=10)

# slider
def slider_event(value):    
    # cancel any previously scheduled brightness change
    if hasattr(app, "brightness_change_id"):
        app.after_cancel(app.brightness_change_id)
    
    # schedule the brightness change after a delay of 500 ms
    app.brightness_change_id = app.after(500, set_brightness, int(value))

# set brightness with display
def set_brightness(value):
    sbc.set_brightness(value, data["display"])

slider = ctk.CTkSlider(frame_top, from_=0, to=100, width=256, height=32, command=slider_event)
# starts with the primary display brightness value
slider.set(sbc.get_brightness(0)[0])
slider.grid(row=0, column=1)

# combobox
def combobox_callback(choice):
    # selected display index
    display = int(choice) - 1

    # append selected display index
    data["display"] = display
    
    # set the slider value to selected display brightness level
    slider.set(int(sbc.get_brightness(display)[0]))

combobox = ctk.CTkComboBox(frame_top, values=[str(i+1) for i in range(len(sbc.list_monitors()))], width=56, command=combobox_callback)
combobox.grid(row=0, column=2, padx=10)

# button
theme_image = ctk.CTkImage(light_image=Image.open("resources/dark.png"),
                        dark_image=Image.open("resources/light.png"),
                        size=(32, 32))

def theme_button_event():
    if data["theme"] == "light":
        data["theme"] = "dark"
    else:
        data["theme"] = "light"

    ctk.set_appearance_mode(data["theme"])

theme_button = ctk.CTkButton(frame_bottom, text="", width=40, height=40, image=theme_image, command=theme_button_event)
theme_button.grid(row=0, column=0)

update_image = ctk.CTkImage(light_image=Image.open("resources/update-light.png"),
                        dark_image=Image.open("resources/update-dark.png"),
                        size=(32, 32))

update_button = ctk.CTkButton(frame_bottom, text="", width=40, height=40, image=update_image)
update_button.grid(row=0, column=1, padx=10)

def settings_button_event():
    main_frame.grid_remove()
    settings_frame.grid(row=0, column=0)

settings_image = ctk.CTkImage(light_image=Image.open("resources/settings-light.png"),
                        dark_image=Image.open("resources/settings-dark.png"),
                        size=(32, 32))

settings_button = ctk.CTkButton(frame_bottom, text="", width=40, height=40, image=settings_image, command=settings_button_event)
settings_button.grid(row=0, column=2)

# mainloop
app.mainloop()