from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics
import requests
import webbrowser
import os

version = 1.4

root = Tk()
root.title("Updater")

screen_width = 420
screen_height = 178
root.geometry(f"{screen_width}x{screen_height}+"
              f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

root.resizable(False, False)

root.iconbitmap(r"C:/x86 INSIDE/Brightness Control/script/Brightness Control.ico")

status_label = ttk.Label(root, text=" You are already running the latest version ! ", font="Ariel, 15")
status_label.pack(pady=50)


def update():
    webbrowser.open_new_tab("https://sourceforge.net/projects/brightness-control/")
    os.startfile(r"C:/x86 INSIDE/Brightness Control/script/script_bat_4.bat")


update_button = ttk.Button(root, text="Update", command=update)
update_button.pack(ipadx=22, ipady=5)


def configure():
    def update_checker():
        try:
            check = float(requests.get('https://raw.githubusercontent.com/muyeed15/Brightness_Control/main/info.txt').text)

            if check > version:
                status = " Updates are available ! "
                status_color = "Red"

                status_label.config(text=status, foreground=status_color)

                update_button["state"] = "enable"

            else:
                status = " You are already running the latest version ! "
                status_color = "#279145"

                status_label.config(text=status, foreground=status_color)

                update_button["state"] = "disabled"


        except:
            status = " No Internet ! "
            status_color = "Gray"

            status_label.config(text=status, foreground=status_color)

            update_button["state"] = "disabled"

    update_checker()

    root.after(1000, configure)


configure()

root.mainloop()
