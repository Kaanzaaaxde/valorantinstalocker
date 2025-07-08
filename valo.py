import pyautogui as pg
import tkinter as tk
from tkinter import Label, Button
from pynput import keyboard
import threading
import time

# GUI Penceresi
window = tk.Tk()
window.geometry("400x200")
window.title("Neon Instapick")
window.resizable(False, False)

# Durum bayrağı
stop_flag = False


def pick_neon():
    global stop_flag
    stop_flag = False
    Label(window, text="Neon seçiliyor…", fg='black', font=("Helvetica", 12)) \
        .grid(row=2, column=0, padx=20, pady=(10,0), columnspan=2)
    start_time = time.time()
    while time.time() - start_time < 10:  # 10 saniye boyunca tıklama
        pg.moveTo(210, 530)
        pg.click()
        pg.PAUSE = 0.035
        pg.moveTo(713, 600)
        pg.click()
        if stop_flag:
            print("Loop durduruldu: P tuşuna basıldı")
            break
    window.quit()  # GUI penceresini kapat

def on_press(key):
    global stop_flag
    try:
        if key.char == 'n':
            threading.Thread(target=pick_neon, daemon=True).start()
        elif key.char == 'p':
            stop_flag = True
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Klavye dinleyicisi
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# GUI Butonu
Button(window, text='Pick Neon', command=lambda: threading.Thread(target=pick_neon, daemon=True).start(),
       fg='magenta', font=("Helvetica", 14)) \
    .grid(row=0, column=0, padx=20, pady=20)

# Bilgi Etiketi
Label(window, text="Press 'N' to pick Neon (global)\nPress 'P' to stop", 
      fg='black', font=('Helvetica', 12)) \
    .grid(row=1, column=0, padx=20)



if __name__ == "__main__":
    window.mainloop()
