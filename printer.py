#!/usr/bin/env python3
import string
import random
import os
import sys
import tkinter as tk
from sys import platform
from selenium import webdriver
from tkinter import ttk


class myTest:
    def __init__(self):

        # if user is on Windows
        if platform == "win32":
            self.driver = webdriver.Chrome()
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")

        # if user is on Linux
        elif platform == "linux" or platform == "linux2":
            self.driver = webdriver.Firefox()
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("-private")

        # if user is on Mac
        else:
            print("Get a PC you pleb")
            sys.exit()

    def refresh(self):
        random_string = get_random_string(6)
        url = "https://prnt.sc/" + random_string
        self.driver.get(url)



def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    numbers = '1234567890'
    result_str = ''.join(random.choice(letters + numbers) for i in range(length))
    return result_str



def click():
    action.configure(text="Clicked")


if __name__ == '__main__':
    test = myTest()
    test.refresh()
    win = tk.Tk()
    win.geometry("200x50")
    win.title('GUI')
    Lbl = ttk.Label(win)
    Lbl.pack()  # Click event
    Lbl.configure(foreground='red')
    action = ttk.Button(win, text="Click Me", command=lambda: test.refresh())
    action.pack()
    win.mainloop()
