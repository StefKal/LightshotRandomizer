import string
import random
import os
from selenium import webdriver
import tkinter as tk
from tkinter import ttk
from sys import platform
import sys


class BrowserDriver:
    def __init__(self):
        self.url_list = []
        self.current_url = 0
        # if user is on Windows
        if platform == "win32":
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            options.add_argument("headless")
            self.driver = webdriver.Chrome(options=options)

        # if user is on Linux
        elif platform == "linux" or platform == "linux2":
            options = webdriver.FirefoxOptions()
            options.headless = True
            self.driver = webdriver.Firefox(options=options)

        # if user is on Mac
        else:
            print("Get a PC you pleb")
            sys.exit()

    # generate a random URL, get it and screenshot the page
    def save_image(self, url):
        self.driver.get(url)

        image_div = self.driver.find_element_by_class_name("under-image")
        image_div.find_element_by_tag_name('img').screenshot('image.png')

    def get_random_url(self):
        random_string = get_random_string(6)
        url = "https://prnt.sc/" + random_string
        self.url_list.append(url)
        self.current_url = len(self.url_list) - 1
        return self.url_list[self.current_url]

    def next_url(self):
        if self.current_url != len(self.url_list) - 1:
            self.current_url += 1
        return self.url_list[self.current_url]

    def prev_url(self):
        if self.current_url != 0:
            self.current_url -= 1
        return self.url_list[self.current_url]


class UI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.prevImage = tk.Button(self)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.master = master
        self.pack()
        self.canvas = tk.Canvas()
        self.driver = BrowserDriver()
        self.create_widgets()
        self.quit.pack(side="bottom")

    def random(self):
        url = self.driver.get_random_url()
        self.refresh_ui(url)

    def next(self):
        url = self.driver.next_url()
        self.refresh_ui(url)

    def previous(self):
        url = self.driver.prev_url()
        self.refresh_ui(url)

    # Creates next putton and adds listener to it
    def create_widgets(self):
        self.randomImage = tk.Button(self, text="Random", command=lambda: self.random()).pack()
        self.nextImage = tk.Button(self, text="Next", command=lambda: self.next()).pack()
        self.prevImage = tk.Button(self, text="Prev", command=lambda: self.previous()).pack()

    # saves, zooms and refreshes image on TKinter GUI
    def first_update(self):
        url = self.driver.get_random_url()
        self.driver.save_image(url)
        self.img = tk.PhotoImage(file="image.png")
        self.img = self.img.zoom(2)
        self.label = ttk.Label(image=self.img)
        self.label.pack()

    def refresh_ui(self, url):
        self.driver.save_image(url)
        self.img = tk.PhotoImage(file="image.png")
        self.label['image'] = self.img
        self.label.photo_ref = self.img

    # key event for right arrow to refresh the UI
    def key_handler(self, event):
        if event.keycode == 39:
            self.refresh_ui()


# generate a random URL
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    numbers = '1234567890'
    result_str = ''.join(random.choice(letters + numbers) for i in range(length))
    return result_str


if __name__ == '__main__':
    root = tk.Tk()
    app = UI(master=root)
    root.bind("<Key>", app.key_handler)
    app.first_update()
    app.mainloop()
