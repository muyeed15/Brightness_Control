import os
from tkinter import *
from tkinter import ttk
from win32api import GetSystemMetrics

x = os.environ.get('USERNAME')

root = Tk()
root.title("Settings")

screen_width = 362
screen_height = 188
root.geometry(f"{screen_width}x{screen_height}+"
              f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

root.resizable(False, False)

root.iconbitmap(r"C:/x86 INSIDE/Brightness Control/script/Brightness Control.ico")

settings_label = ttk.Label(root, text="Settings       ", font="Ariel, 20", foreground="#ff8900")
settings_label.grid(row=0, column=0, ipady=10)
start_label = ttk.Label(root, text="   Run in the start-up          ", font="Ariel", foreground="Gray")
start_label.grid(row=1, column=0, ipady=10)

var_0 = IntVar()

if os.path.exists(str("C:" + r"\Users" + f"\{x}" + r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Brightness Control.lnk")):
    var_0.set(1)
else:
    var_0.set(0)


def yes_0():
    os.startfile(r"C:/x86 INSIDE/Brightness Control/script/script_bat_0.bat")


def no_0():
    os.startfile(r"C:/x86 INSIDE/Brightness Control/script/script_bat_1.bat")


yes_label_0 = ttk.Label(root, text="    Yes ", font="Ariel", foreground="Green")
yes_label_0.grid(row=1, column=1)
yes_radio_0 = ttk.Radiobutton(root, variable=var_0, value=1, command=yes_0)
yes_radio_0.grid(row=1, column=2)

no_label_0 = ttk.Label(root, text="        No ", font="Ariel", foreground="Red")
no_label_0.grid(row=1, column=3)
no_radio_0 = ttk.Radiobutton(root, variable=var_0, value=0, command=no_0)
no_radio_0.grid(row=1, column=4)

start_label = ttk.Label(root, text="    Minimize in the start-up   ", font="Ariel", foreground="Gray")
start_label.grid(row=2, column=0, ipady=10)

var_1 = IntVar()

if int(open(r"C:/x86 INSIDE/Brightness Control/script/script_dat_1.txt", "r").read()) == 1:
    var_1.set(1)
else:
    var_1.set(0)


def yes_1():
    open(r"C:/x86 INSIDE/Brightness Control/script/script_dat_1.txt", "w").write("1")


def no_1():
    open(r"C:/x86 INSIDE/Brightness Control/script/script_dat_1.txt", "w").write("0")


yes_label_1 = ttk.Label(root, text="    Yes ", font="Ariel", foreground="Green")
yes_label_1.grid(row=2, column=1)
yes_radio_1 = ttk.Radiobutton(root, variable=var_1, value=1, command=yes_1)
yes_radio_1.grid(row=2, column=2)

no_label_1 = ttk.Label(root, text="        No ", font="Ariel", foreground="Red")
no_label_1.grid(row=2, column=3)
no_radio_1 = ttk.Radiobutton(root, variable=var_1, value=0, command=no_1)
no_radio_1.grid(row=2, column=4)

dev_label = ttk.Label(root, text="Developed By Muyeed               ", font="Ariel, 8", foreground="Gray")
dev_label.grid(row=3, column=0, ipady=10)

root.mainloop()
