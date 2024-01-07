# modules
from customtkinter import *
from tkinter import *
from tkinter import ttk
import screen_brightness_control
import requests
import webbrowser
import os
from win32api import GetSystemMetrics
import getpass
import shutil
from win32com.client import Dispatch

# app
version = "1.5.0"

stored_data = 100

try:
    new_version = requests.get("https://raw.githubusercontent.com/muyeed15/Brightness_Control/main/version.txt").text
except:
    new_version = "null"

def save():
    open(fr"C:\EVOKE\Brightness Control\config.ini", "w").write(str(stored_data))


def rem_x86():
    try:
        shutil.rmtree(fr"C:\x86 INSIDE\Brightness Control")
    except: pass


def srt_up_on():
    try:
        user_name = getpass.getuser()

        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(fr"C:\Users\{user_name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Brightness Control.lnk")
        shortcut.Targetpath = fr"C:\EVOKE\Brightness Control\Brightness Control.exe"
        shortcut.save()
    except: pass


try:
    stored_data = int(open(fr"C:\EVOKE\Brightness Control\config.ini", "r").read())
except:
    save()
    rem_x86()
    srt_up_on()

screen_brightness_control.set_brightness(stored_data, display=0)

# main gui
app = Tk()

app.title("Brightness Control")
app.iconbitmap(fr"C:/EVOKE/Brightness Control/resources/Brightness Control.ico")

screen_width = 471
screen_height = 168
app.geometry(f"{screen_width}x{screen_height}+"
              f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

app.resizable(False, False)

slider_value_code = IntVar()

def get_slider_value():
    return format(slider_value_code.get())


value = Label(app, text=str(stored_data), font="Arial, 25", foreground="gray")

app.brightness_change_id = None

def set_brightness_after_delay():
    global stored_data
    screen_brightness_control.set_brightness(get_slider_value(), display=0)
    stored_data = int(get_slider_value())
    save()


def slider_change(event):
    value.config(text=get_slider_value())
    
    if app.brightness_change_id:
        app.after_cancel(app.brightness_change_id)
    
    app.brightness_change_id = app.after(500, set_brightness_after_delay)


bcon = Label(app, text=" Brightness  :", font="Arial, 25", foreground="#ff8900")
bcon.grid(row=0, column=0)

slider = CTkSlider(app, from_=0, to=100, width=257, variable=slider_value_code, command=slider_change)
slider.set(stored_data)
slider.grid(row=0, column=1, padx=8, pady=20, ipady=5)

level = Label(app, text=" Level           :", font="Arial, 25", foreground="gray")
level.grid(row=1, column=0)

value.grid(row=1, column=1)

if (new_version == version) or (new_version == "null"):
    ver_tex = " Version: " + str(version) +" "*34
    ver_col = "gray"
else:
    ver_tex = " Updates are available! " + " "*20
    ver_col = "red"

ver_label = Label(app, text=ver_tex, font="Ariel, 8", foreground=ver_col)
ver_label.grid(row=2, column=0)

frame = ttk.Frame(app)
frame.grid(row=2, column=1, pady=13)

# settings
def settings():
    user_name = getpass.getuser()
    dst_path = fr"C:\Users\{user_name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Brightness Control.lnk"

    set_default_color_theme("green")

    app_set = Toplevel()

    app_set.title("Settings")
    app_set.iconbitmap(fr"C:/EVOKE/Brightness Control/resources/Brightness Control.ico")

    screen_width = 471
    screen_height = 168
    app_set.geometry(f"{screen_width}x{screen_height}+"
                f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

    app_set.resizable(False, False)

    set = Label(app_set, text=" Settings "+ " "*23, font="Arial, 25", foreground="#ff8900")
    set.grid(row=0, column=0, pady=5)

    srt = Label(app_set, text="Run Brightness Control in the start-up" + " "*15 +":", font="Ariel, 12", foreground="gray")
    srt.grid(row=1, column=0, pady=5)

    def str_up_off():
        try:
            os.remove(dst_path)
        except: pass


    def switch_event():
        if switch_var.get() == "on":
            srt_up_on()
        else:
            str_up_off()


    if os.path.exists(fr"C:\Users\{user_name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Brightness Control.lnk") == False:
        srt_st = "off"
    else:
        srt_st = "on"

    switch_var = StringVar(value=srt_st)
    srt_switch = CTkSwitch(app_set, text="  off/on", fg_color="#fc5656",command=switch_event, variable=switch_var, onvalue="on", offvalue="off")
    srt_switch.grid(row=1, column=1)

    dev_vis = Label(app_set, text="Visit my GitHub Profile" + " "*40 +":", font="Ariel, 12", foreground="gray")
    dev_vis.grid(row=2, column=0)

    def git_link():
        webbrowser.open_new_tab("https://github.com/muyeed15/")


    dev_butt = ttk.Button(app_set, text="GitHub", command=git_link)
    dev_butt.grid(row=2, column=1, ipadx=18, ipady=3, pady=5)

    dev_label = Label(app_set, text="Developed By Muyeed", font="Ariel, 8", foreground="gray")
    dev_label.grid(row=3, column=1, ipady=10)

    app_set.mainloop()


settings_button = ttk.Button(frame, text="Settings", command=settings)
settings_button.grid(row=0, column=0, ipadx=22, ipady=3)

# update
update_button = ttk.Button(text="Update")

def update():
    try:
        new_version = requests.get("https://raw.githubusercontent.com/muyeed15/Brightness_Control/main/version.txt").text
    except:
        new_version = "null"
    
    app_update = Toplevel(app)
    app_update.title("Updater")
    app_update.iconbitmap(fr"C:/EVOKE/Brightness Control/resources/Brightness Control.ico")

    ver_dat = version

    def web_link():
        webbrowser.open_new_tab("https://sourceforge.net/projects/brightness-control/")
        app.destroy()

    web_button = ttk.Button(app_update, text="Download", command=web_link, state="disabled")

    if new_version == "null":
        data = "📶 Error: Connection Failed! 📶"
        color = "gray"
    
    elif new_version == version:
        data = "⚡ You're On The Latest Version ⚡"
        color = "#279145"

    else:
        data = f"✦ Enhance Your Experience ✦"
        color = "#ff8900"
        ver_dat =  f" {version} » {new_version} "
        web_button["state"] = "enabled"

    blank = Label(app_update, text=" ")
    blank.pack()

    status_label = Label(app_update, text=data, font="Ariel, 20", foreground=color)
    status_label.pack(pady=3)

    version_label = Label(app_update, text="[ " + ver_dat + " ]", font="Ariel, 12", foreground="gray")
    version_label.pack(pady=15)

    web_button.pack(ipadx=22, ipady=3, pady=4)

    app_update.geometry(f"{screen_width}x{screen_height}+"
                f"{int((GetSystemMetrics(0) - screen_width) / 2)}+{int((GetSystemMetrics(1) - screen_height) / 2)}")

    app_update.resizable(False, False)

    app_update.mainloop()


update_button = ttk.Button(frame, text="Check Update", command=update)
update_button.grid(row=0, column=1, ipadx=22, ipady=3)

app.mainloop()

