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

# frame
frame_top = ctk.CTkFrame(app, fg_color="transparent")
frame_top.pack()

frame_mid = ctk.CTkFrame(app, fg_color="transparent")
frame_mid.pack()

# top image
top_image = ctk.CTkImage(light_image=Image.open("resources/sun.png"),
                        dark_image=Image.open("resources/moon.png"),
                        size=(56, 56))

top_image_label = ctk.CTkLabel(frame_top, image=top_image, text="")
top_image_label.grid(row=0, column=0, padx=10, pady=10)

# slider
def slider_event(value):
    label.configure(text=int(value))
    
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
    
    # set the slider and label values to selected display brightness level
    slider.set(int(sbc.get_brightness(display)[0]))
    label.configure(text=int(sbc.get_brightness(display)[0]))

combobox = ctk.CTkComboBox(frame_top, values=[str(i+1) for i in range(len(sbc.list_monitors()))], width=56, command=combobox_callback)
combobox.grid(row=0, column=2, padx=10, pady=10)

# label
label = ctk.CTkLabel(frame_mid, text=int(slider.get()), font=("", 32), text_color=("gray", "gray"), fg_color="transparent")
label.pack()

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

theme_button = ctk.CTkButton(app, text="", width=40, height=40, image=theme_image, command=theme_button_event)
theme_button.pack()

# mainloop
app.mainloop()