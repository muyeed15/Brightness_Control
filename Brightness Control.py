import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import screen_brightness_control
from win32api import GetSystemMetrics
import requests
import pystray
from pystray import MenuItem as item
from PIL import Image

# Make sure that you are running this code in this directory: "C:\x86 INSIDE\Brightness Control"
# This program was originally designed to run in Windows Operating System only

version = 1.4

if int(open(r"C:/x86 INSIDE/Brightness Control/script/script_dat_2.txt", "r").read()) == 0:
    messagebox.showinfo("Brightness Control", "Thank you for installing Brightness Control!")
    os.startfile(r"C:\x86 INSIDE\Brightness Control\script\script_bat_0.bat")
    open(r"C:/x86 INSIDE/Brightness Control/script/script_dat_2.txt", "w").write("1")
else:
    pass

root = Tk()
root.title("Brightness Control")

screen_width = 447
screen_height = 155
root.geometry(f"{screen_width}x{screen_height}+"
              f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

root.resizable(False, False)

root.iconbitmap(r"C:/x86 INSIDE/Brightness Control/script/Brightness Control.ico")
icon_system_tray = Image.open(r"C:/x86 INSIDE/Brightness Control/script/Brightness Control.ico")

slider_value_code = IntVar()


def get_slider_value():
    return format(slider_value_code.get())


value_0 = ttk.Label(root, text=get_slider_value(), font="Ariel, 20", foreground="Gray")
value_0.grid(row=1, column=1, columnspan=5, ipady=10)


def slider_change(event):
    screen_brightness_control.set_brightness(get_slider_value(), display=0)
    value_0.config(text=get_slider_value())
    open(r"C:/x86 INSIDE/Brightness Control/script/script_dat_0.txt", "w").write(get_slider_value())


slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", variable=slider_value_code, command=slider_change)
slider.set(open(r"C:/x86 INSIDE/Brightness Control/script/script_dat_0.txt", "r").read())
slider.grid(row=0, column=4, columnspan=4, ipadx=73)

brightness_label = ttk.Label(root, text=" Brightness    : ", font="Ariel, 20", foreground="#ff8900")
brightness_label.grid(row=0, column=0, columnspan=4, ipady=10)

amount_label = ttk.Label(root, text=" Amount        : ", font="Ariel, 20", foreground="Gray")
amount_label.grid(row=1, column=0, columnspan=4, ipady=10)

status_label = ttk.Label(root, text=" Version: " + str(version) + " " * 36, font="Ariel, 8", foreground="Gray")
status_label.grid(row=2, column=0, columnspan=4, ipady=10)


def configure():
    def update_checker():
        try:
            check = float(requests.get('https://raw.githubusercontent.com/muyeed15/Brightness_Control/main/info.txt').text)

            if check > version:
                status = " Updates are available! " + " " * 21
                status_color = "Red"

                status_label.config(text=status, foreground=status_color)

            else:
                status = " Version: " + str(version) + " " * 36
                status_color = "Gray"

                status_label.config(text=status, foreground=status_color)


        except:
            status = " No Internet " + " " * 37
            status_color = "Gray"

            status_label.config(text=status, foreground=status_color)

    update_checker()

    root.after(1000, configure)


configure()


def quit_window(icon, item):
    icon.stop()
    root.destroy()


def show_window(icon, item):
    icon.stop()
    root.after(0, root.deiconify())


def hide_window():
    root.withdraw()
    menu = (item("Brightness Control", show_window, default=True), item("Quit", quit_window))
    icon = pystray.Icon("Brightness Control", icon_system_tray, "Brightness Control", menu)
    icon.run()


root.protocol("WM_DELETE_WINDOW", hide_window)


def settings():
    #os.startfile(r"C:\x86 INSIDE\Brightness Control\script\script_bat_2.bat")     # This option is enabled in the executable file
    os.startfile(r"C:\x86 INSIDE\Brightness Control\script\Settings.py")           # This option is disabled in the executable file


settings_button = ttk.Button(root, text="Settings", command=settings)
settings_button.grid(row=2, column=4, ipadx=22, ipady=3)


def update():
    #os.startfile(r"C:\x86 INSIDE\Brightness Control\script\script_bat_3.bat")     # This option is enabled in the executable file
    os.startfile(r"C:\x86 INSIDE\Brightness Control\script\Updater.py")            # This option is disabled in the executable file


update_button = ttk.Button(root, text="Check Update", command=update)
update_button.grid(row=2, column=5, ipadx=22, ipady=3)

if int(open(r"C:/x86 INSIDE/Brightness Control/script/script_dat_1.txt", "r").read()) == 1:
    hide_window()
else:
    pass

root.mainloop()
