import tkinter as tk
from tkinter import ttk, messagebox
import os
import screen_brightness_control as sbc
import requests
import webbrowser
import pystray
from pystray import MenuItem as item
from PIL import Image

title = 'Brightness Control'
version = 1.1


def full_process():
    root = tk.Tk()
    root.title(title)
    root.iconbitmap('data\\icons\\Brightness Control.ico')
    icon_system_tray = Image.open('data\\icons\\Brightness Control.ico')
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')

    def update_checker_online():
        try:
            version_check = float(requests.get(
                'https://raw.githubusercontent.com/muyeed15/Brightness-Control-Updates/master/'
                'version.txt').text.strip())
            if version_check > version:
                webbrowser.open_new_tab(
                    'https://github.com/muyeed15/Brightness-Control-Updates/blob/master/Brightness_Control_Update.exe'
                    '?raw=true')
            else:
                messagebox.showinfo(title, 'You are running the latest version!')
        except requests.RequestException:
            messagebox.showinfo(title, 'Please check your internet connection!\nUnable to check for updates!')

    try:
        version_check_request = requests.get(
            'https://raw.githubusercontent.com/muyeed15/Brightness-Control-Updates/master/version.txt')
        version_check = float(version_check_request.text.strip())
        with open('data\\scripts\\written_version.txt', 'w') as written_version:
            written_version.write(str(version_check))
        with open('data\\scripts\\written_version.txt', 'r') as reading_version:
            value_version = float(reading_version.read().strip())
        if value_version > version:
            root.geometry('359x139')
            update_button_text = 'Install Updates'
            version_or_update = f'Updates are available!\nCurrent Version: {version}\nLatest Version: {value_version}'
            update_button = ttk.Button(root, text=update_button_text, command=update_checker_online)
            update_button.grid(row=2, column=2, ipadx=20, ipady=2)
            update_notifier = ttk.Label(root, text=version_or_update, foreground='red')
            update_notifier.grid(row=1, column=2)
        else:
            root.geometry('361x114')
            update_button_text = 'Check Updates'
            version_or_update = f'Version: {version}'
            update_button = ttk.Button(root, text=update_button_text, command=update_checker_online)
            update_button.grid(row=2, column=2, ipadx=20, ipady=2)
            update_notifier = ttk.Label(root, text=version_or_update)
            update_notifier.grid(row=1, column=2, ipady=10)
    except requests.RequestException:
        messagebox.showinfo(title, 'Please check your internet connection!\nUnable to check for updates!')

    slider_values = tk.DoubleVar()
    brightness_level = ttk.Label(root, text='Brightness:')
    brightness_level.grid(row=0, column=0, columnspan=1, ipady=10)

    def get_slider_values():
        return '{:.2f}'.format(slider_values.get())

    def slider_changed(event=None):
        value_label.config(text=get_slider_values())
        sbc.set_brightness(get_slider_values())

    def value_writer():
        with open('data\\scripts\\written_value.txt', 'w') as written_value:
            written_value.write(get_slider_values())
        messagebox.showinfo(title, 'Brightness data saved!')

    def mail():
        webbrowser.open('mailto:muyeed.al.abdullah@outlook.com')

    def git():
        webbrowser.open('https://github.com/muyeed15')

    with open('data\\scripts\\startup.txt', 'r') as reading_startup:
        value_startup = float(reading_startup.read().strip())
    main_startup = 0
    if value_startup > main_startup:
        startup_text = '   ↓ Click the button down below to not run Brightness Control in the startup ↓   '
        startup_button_text = 'Do not run in the startup'
    else:
        startup_text = '   ↓ Click the button down below to run Brightness Control in the startup ↓   '
        startup_button_text = 'Run in the startup'

    def startup_script():
        if value_startup > main_startup:
            os.system('data\\scripts\\startup_del.bat')
            with open('data\\scripts\\startup.txt', 'w') as written_startup:
                written_startup.write('0.00')
            messagebox.showinfo(title, 'Brightness Control will not run in the startup!')
        else:
            os.system('data\\scripts\\startup.bat')
            with open('data\\scripts\\startup.txt', 'w') as written_startup:
                written_startup.write('1.00')
            messagebox.showinfo(title, 'Brightness Control will run in the startup!')
        root.quit()

    def restore():
        with open('data\\scripts\\process_info.txt', 'w') as process_write:
            process_write.write('0.00')
        with open('data\\scripts\\startup.txt', 'w') as written_startup:
            written_startup.write('1.00')
        with open('data\\scripts\\written_value.txt', 'w') as written_value:
            written_value.write('100.00')
        os.system('data\\scripts\\startup_del.bat')
        messagebox.showinfo(title, 'Settings are now restored!')
        root.quit()

    def settings():
        root_settings = tk.Tk()
        root_settings.title('Settings')
        root_settings.iconbitmap('data\\icons\\Brightness Control.ico')
        root_settings.resizable(False, False)
        root_settings.eval('tk::PlaceWindow . center')
        monitor_label = ttk.Label(root_settings, text='↓ Connected Monitors ↓')
        monitor_label.pack(ipady=5)
        monitors = sbc.list_monitors()
        monitors_list_label = ttk.Label(root_settings, text=str(monitors), background='#F6931E')
        monitors_list_label.pack(ipady=5)
        run_start_up_label = ttk.Label(root_settings, text=startup_text)
        run_start_up_label.pack(ipady=5)
        run_start_up_button = ttk.Button(root_settings, text=startup_button_text, command=startup_script)
        run_start_up_button.pack(ipady=5)
        ttk.Label(root_settings, text='-------------------------------------------------------------------------------',
                  foreground='#F6931E').pack(ipady=5)
        restore_label = ttk.Label(root_settings, text='↓ Click the button down below to restore defaults ↓')
        restore_label.pack(ipady=5)
        restore_button = ttk.Button(root_settings, text='Restore Defaults', command=restore)
        restore_button.pack(ipady=5)
        ttk.Label(root_settings, text='-------------------------------------------------------------------------------',
                  foreground='#F6931E').pack(ipady=5)
        ttk.Label(root_settings, text='Thank you for using Brightness Control!').pack(ipady=5)
        ttk.Label(root_settings, text='⚡ This program was developed by Muyeed ⚡').pack(ipady=5)
        ttk.Button(root_settings, text='☛ GitHub: https://github.com/muyeed15 ☚', command=git).pack(ipady=5)
        ttk.Label(root_settings, text='   ↓ Click the button down below to send feedbacks ↓   ').pack(ipady=10)
        ttk.Button(root_settings, text='Feedback', command=mail).pack(ipady=10, ipadx=20)
        root_settings.mainloop()

    with open('data\\scripts\\written_value.txt', 'r') as reading_value:
        value_reader = reading_value.read().strip()
    sbc.set_brightness(value_reader)
    value_label = ttk.Label(root, text=get_slider_values())
    value_label.grid(row=1, column=1)
    slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=slider_values)
    slider.set(value_reader)
    slider.grid(row=0, column=1, columnspan=3, padx=10, ipadx=50, ipady=10)
    value_amount = ttk.Label(root, text='Amount      :')
    value_amount.grid(row=1, column=0, columnspan=1)
    save_button = ttk.Button(root, text='Save', command=value_writer)
    save_button.grid(row=2, column=0, ipadx=20, ipady=2)
    settings_button = ttk.Button(root, text='Settings', command=settings)
    settings_button.grid(row=2, column=1, ipadx=20, ipady=2)

    def quit_window(icon=None, item=None):
        icon.stop()
        root.destroy()

    def show_window(icon=None, item=None):
        icon.stop()
        root.after(0, root.deiconify())

    def hide_window():
        root.withdraw()
        menu = (item(str(title), show_window, default=True), item('Quit', quit_window))
        icon = pystray.Icon(str(title), icon_system_tray, str(title), menu)
        icon.run()

    root.protocol('WM_DELETE_WINDOW', hide_window)
    hide_window()
    root.mainloop()


def startup_writer():
    with open('data\\scripts\\process_info.txt', 'w') as process_write:
        process_write.write('1.00')


def main():
    with open('data\\scripts\\process_info.txt', 'r') as reading_process:
        process_code = float(reading_process.read().strip())
    try:
        if process_code < 1.0:
            os.system('data\\scripts\\startup.bat')
            startup_writer()
            messagebox.showinfo(title, 'Thank You for installing Brightness Control!')
            full_process()
    finally:
        full_process()


if __name__ == "__main__":
    main()
